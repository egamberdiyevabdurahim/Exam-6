from django.urls import path

from users.views import login_view, register_view, logout_view, verify_email


app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify-email'),
]