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
from users.form import RegisterForm, LoginForm
from users.token import email_token_generator


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
            return redirect(reverse_lazy('users:login'))
    except Exception:
        return redirect(reverse_lazy('users:login'))


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


def login_view(request):
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
                    return redirect(reverse_lazy('home'))
                else:
                    return render(request, 'auth/login.html', {
                        'error': 'Invalid login details or account not activated. Please check your email.'
                    })
            else:
                return render(request, 'auth/login.html', {'error': 'Username of Password error'})

    else:
        return render(request, 'auth/login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            send_email_verification(request, user)
            return redirect(reverse_lazy('users:login'))
        else:
            errors = form.errors
            print("-"*50)
            print(errors)
            print("-"*50)
            return render(request, 'auth/register.html', {'errors': errors})
    else:
        return render(request, 'auth/register.html')


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('home'))
