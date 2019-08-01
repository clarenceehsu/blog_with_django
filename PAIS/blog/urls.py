from django.urls import path
from django.urls import re_path
from blog import views as blog_views


app_name = 'blog'

urlpatterns = [
    # path('', blog_views.post_list, name='post_list'), # 列表页的url规则
    path('', blog_views.index, name='blog'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', blog_views.detail, name='detail'),
]