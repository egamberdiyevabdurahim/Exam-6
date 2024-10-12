from django.urls import path, re_path

from post.views import create_offer_view, create_problem_view, offers_problems_view, offer_detail_view, \
    offer_comment_poster_view, problem_comment_poster_view, problem_detail_view, like_offer_view, like_problem_view, \
    like_offer_comment_view, like_problem_comment_view

app_name = 'post'

urlpatterns = [
    path('create_offer/', create_offer_view, name='create_offer'),
    path('create_problem/', create_problem_view, name='create_problem'),
    path('offer_problem/', offers_problems_view, name='offer_problem'),
    re_path(r'^offer/(?P<pk>[0-9]+)/(?P<url>[\w\-_]+)$', offer_detail_view, name='offer_detail'),
    re_path(r'^problem/(?P<pk>[0-9]+)/(?P<url>[\w\-_]+)$', problem_detail_view, name='problem_detail'),
    path('problem/<int:pk>/', problem_detail_view, name='problem_detail'),
    path('offer/comment_poster/<int:pk>/', offer_comment_poster_view, name='offer_comment_poster'),
    path('problem/comment_poster/<int:pk>/', problem_comment_poster_view, name='problem_comment_poster'),
    path('like_offer/<int:pk>/', like_offer_view, name='like_offer'),
    path('like_problem/<int:pk>/', like_problem_view, name='like_problem'),
    path('like_offer_comment/<int:pk>/', like_offer_comment_view, name='like_offer_comment'),
    path('like_problem_comment/<int:pk>/', like_problem_comment_view, name='like_problem_comment'),
]