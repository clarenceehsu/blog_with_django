import os
import markdown

def get_post_list(filepath):
    list = []
    dir_list = os.listdir(filepath)
    image = ''

    for i in [n for n in dir_list if n.split('.')[-1] == 'md']:
        with open('/root/PAIS/_posts/' + i, 'r') as f:
            post = f.readlines()
            for n in post:
                if 'date: ' in n:
                    date = n.split(': ')[-1].split(' ')[0].strip().split('-')
                elif 'title: ' in n:
                    title = n.split(': ')[-1].strip()
                elif 'thumbnailImage: ' in n:
                    image = n.split(': ')[-1].strip()
                    break
        time = date[0] + '年' + str(int(date[1])) + '月' + date[2] + '日'
        list.append([time, title, image])
        image = ''
    return reversed(sorted(list))

def get_post(name):
    index = 0
    post, cover = '', ''
    with open('/root/PAIS/_posts/' + name + '.md', 'r') as f:
        detail = f.readlines()
        for n in detail:
            if index == 2:
                post += n
            elif n == '---\n':
                index += 1
            elif 'date: ' in n:
                time = n.split(': ')[-1].split(' ')[0].strip()
            elif 'title: ' in n:
                title = n.split(': ')[-1].strip()
            elif 'coverImage: ' in n:
                cover = n.split(': ')[-1].strip()
        post = markdown.markdown(post,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return {'title': title, 'post': post, 'time': time, 'cover': cover}


# print(list(get_post_list('/root/PAIS/_posts')))