from django.shortcuts import render, get_object_or_404
from blog.models import Post
import markdown

def index(request, list_num):
    list_num = int(list_num)
    post_num = list(range(1, Post.objects.all().count()//4 + 2))
    post_list = Post.objects.all()[(list_num - 1) * 4:(list_num - 1) * 4 + 4]

    return render(request, "blog.html", context={'post_list': post_list, 'list_num': list_num, 'post_num': post_num, 'final_num': post_num[-1]})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'detail.html', context={'post': post, 'pk': pk})

def index_initial(request):

    list_num = 1
    post_num = list(range(1, Post.objects.all().count()//4 + 2))
    post_list = Post.objects.all()[0:4]
    
    return render(request, "blog.html", context={'post_list': post_list, 'list_num': list_num, 'post_num': post_num})

def match(request, match):
    print(match)
    if match == 'contact':
        return render(request, "contact.html")
    elif match == 'about':
        return render(request, "about.html")
    elif match.isdigit():
        return index(request, match)