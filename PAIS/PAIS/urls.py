from django.contrib import admin
from django.urls import path, include
from gallery import views as gallery_views
from blog import views as blog_views
from frontpage import views as frontpage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery/', gallery_views.index),
    path('blog', include('blog.urls', namespace='blog')),
    path('', frontpage_views.index),
]
