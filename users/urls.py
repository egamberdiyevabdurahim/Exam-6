from django.urls import path, re_path

from users.views import login_view, register_view, logout_view, verify_email, profile_view, profile_edit_view

app_name = 'users'


urlpatterns = [
    re_path('register/(?P<url>[\w\-_]+)$', register_view, name='register'),
    re_path(r'^login/(?P<url>[\w\-_]+)$', login_view, name='login'),
    re_path(r'^logout/(?P<url>[\w\-_]+)$', logout_view, name='logout'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify-email'),
    path('profile/<int:pk>/', profile_view, name='profile'),
    path('edit_profile/<int:pk>/', profile_edit_view, name='edit_profile'),
]
