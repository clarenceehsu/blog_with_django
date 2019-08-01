from django.shortcuts import render, get_object_or_404
from blog.models import Post
import markdown


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, "blog.html", context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'detail.html', context={'post': post})
