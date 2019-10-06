from django.shortcuts import render
# from blog.models import Post
import markdown
from lab import main


ITEM = 10
# ALL_POST = Post.objects.all()
ALL_POST = list(main.get_post_list('/root/PAIS/_posts/'))

def index(request, list_num):
    list_num = int(list_num)
    post_list = ALL_POST[(list_num - 1) * ITEM:list_num * ITEM]
    post_num = list(range(1, len(ALL_POST)//ITEM + 2))

    return render(request, "blog.html",
        context={
            'post_list': post_list,
            'list_num': list_num,
            'post_num': post_num,
            'final_num': post_num[-1]
        })

def lab(request):
    post = main.get_post_list('/root/PAIS/_posts')
    return render(request, 'new_list.html', context={'post_list': post})

def detail(request, name):
    post = main.get_post(name)
    return render(request, 'new_post.html', context=post)

def match(request, match):
    if match == '/contact' or match == '/about' or match == '/projects':
        return eval('render(request, "%s.html")' % (match.split('/')[-1]))
    elif match == '/lab':
        return lab(request)
    elif '/page/' in match:
        return index(request, match.split('/')[-1])
    elif '/post/' in match:
        return detail(request, match.split('/')[-1])
    else:
        return render(request, "blog.html",
            context={
                'post_list': ALL_POST[0:ITEM],
                'list_num': 1,
                'post_num': list(range(1, len(ALL_POST)//ITEM + 2))
                })