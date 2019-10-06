from django.urls import path
from django.urls import re_path
from blog import views as blog_views


app_name = 'blog'

urlpatterns = [
    # re_path(r'^post/(?P<pk>[0-9]+)/$', blog_views.render, name='render'),
    path('<path:match>', blog_views.match, name='match'),
]