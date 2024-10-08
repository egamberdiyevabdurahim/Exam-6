from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from conf.settings import EMAIL_HOST_USER
from users.form import RegisterForm, LoginForm
from users.token import email_token_generator


def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(force_bytes(uidb64)))
        user = User.objects.get(pk=uid)
        if email_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect(reverse_lazy('login'))
        else:
            return redirect(reverse_lazy('login'))
    except Exception as e:
        print(f'Error: {e}')
        return redirect(reverse_lazy('login'))


def send_email_verification(request, user):
    token = email_token_generator.make_token(request.user)
    uid = urlsafe_base64_encode(force_bytes(request.user.pk))
    domain = request.get_host()
    verification_url = reverse('verify-email', kwargs={'uidb64': uid, 'token': token})
    full_url = f'https://{domain}{verification_url}'

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
            username = None
            if ('@', '.com') in username_or_email:
                user_data = User.objects.filter(email=username_or_email.lower()).first()
                if user_data is not None and user_data.is_active:
                    username = user_data.username

            else:
                user_data = User.objects.filter(username=username_or_email.lower()).first()
                if user_data is not None and user_data.is_active:
                    username = username_or_email

            if username is not None:
                user = authenticate(request=request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(reverse_lazy('home'))
                else:
                    return render(request, 'auth/login.html',
                                  {'error': 'Account not activated. Please check your email for verification.'})

            else:
                return render(request, 'auth/login.html', {'error': 'Username or password is incorrect.'})

    else:
        return render(request, 'auth/login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            send_email_verification(request, user)
            return redirect(reverse_lazy('login'))
        else:
            errors = form.errors
            return render(request, 'auth/register.html', {'errors': errors})
    else:
        return render(request, 'auth/register.html')


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('/'))