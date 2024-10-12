from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from conf.settings import EMAIL_HOST_USER
from users.form import RegisterForm, LoginForm, EditProfileForm
from users.models import ProfileModel
from users.token import email_token_generator
from utils.hasher import decode_url


def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if email_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect(reverse_lazy('common:home'))
        else:
            return redirect(reverse_lazy('common:home'))
    except Exception:
        return redirect(reverse_lazy('common:home'))


def send_email_verification(request, user):
    token = email_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    domain = request.get_host()
    verification_url = reverse('users:verify-email', kwargs={'uidb64': uid, 'token': token})
    full_url = f'http://{domain}{verification_url}'

    text_content = render_to_string(
        'auth/verify_email.html',
        {'user': user, 'full_url': full_url}
    )

    message = EmailMultiAlternatives(
        subject='Verify your email',
        body=text_content,
        from_email=EMAIL_HOST_USER,
        to=[user.email]
    )

    message.attach_alternative(text_content, "text/html")
    message.send()


def login_view(request, url=None):
    redirect_url = decode_url(url) if url else '/'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']

            try:
                validate_email(username_or_email)
                is_email = True
            except ValidationError:
                is_email = False

            if is_email:
                user_data = User.objects.filter(email=username_or_email.lower()).first()
                if user_data and user_data.is_active:
                    username = user_data.username
                else:
                    username = None
            else:
                user_data = User.objects.filter(username=username_or_email.lower()).first()
                if user_data and user_data.is_active:
                    username = username_or_email
                else:
                    username = None

            if username:
                user = authenticate(request=request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect(redirect_url)
                else:
                    return render(request, 'auth/login.html', {
                        'form': form,
                        'error': 'Invalid login details or account not activated. Please check your email.',
                        'redirect_url': url,
                        'form_data': request.POST,
                    })
            else:
                return render(request, 'auth/login.html', {
                    'form': form,
                    'error': 'Username or Password error',
                    'redirect_url': url,
                    'form_data': request.POST,
                })
        else:
            return render(request, 'auth/login.html', {
                'form': form,
                'error': 'Invalid form submission',
                'redirect_url': url,
                'form_data': request.POST,
            })
    else:
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form, 'redirect_url': url})


def register_view(request, url):
    redirect_url = decode_url(url)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            ProfileModel.objects.create(
                user_id=user.pk,
            )
            send_email_verification(request, user)
            return redirect(redirect_url)
        else:
            context = {
                'redirect_url': url,
                'errors': form.errors,
                'form_data': request.POST,
            }
            return render(request, 'auth/register.html', context)
    else:
        context = {
            'redirect_url': url,
        }
        return render(request, 'auth/register.html', context)


def logout_view(request, url):
    redirect_url = decode_url(url)
    logout(request)
    return redirect(redirect_url)


def profile_view(request, pk):
    user = User.objects.filter(pk=pk).first()
    context = {
        'user': user,
    }
    return render(request, 'profile/profile.html', context)


def profile_edit_view(request, pk):
    user = User.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            if first_name is None:
                first_name = user.first_name

            last_name = form.cleaned_data['last_name']
            if last_name is None:
                last_name = user.last_name

            organization_name = form.cleaned_data['organization_name']
            if organization_name is None:
                organization_name = user.profile.organization_name

            location = form.cleaned_data['location']
            if location is None:
                location = user.profile.location

            linkedin_url = form.cleaned_data['linkedin_link']
            if linkedin_url is None:
                linkedin_url = user.profile.linkedin_link

            avatar = form.cleaned_data['avatar']
            if avatar is None:
                avatar = user.profile.avatar

            user.first_name = first_name
            user.last_name = last_name
            user.profile.organization_name = organization_name
            user.profile.location = location
            user.profile.linkedin_link = linkedin_url
            user.profile.avatar = avatar
            user.save()
            user.profile.save()
            return redirect(reverse('users:profile', kwargs={'pk': user.pk}))
        else:
            return render(request, 'profile/edit_profile.html', {'user': user})
