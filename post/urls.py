from django.urls import path

from post.views import create_offer_view, create_problem_view


app_name = 'post'

urlpatterns = [
    path('create_offer/', create_offer_view, name='create_offer'),
    path('create_problem/', create_problem_view, name='create_problem'),
]