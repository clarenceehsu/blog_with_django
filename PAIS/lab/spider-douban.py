import requests
from bs4 import BeautifulSoup
import time
from threading import Thread


def request_douban(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def takefirst(elem):
    return elem[0]

def save_file(list):

    try:
        with open('../Top250.csv', 'w+', encoding='utf-8') as dict_file:
            dict_file.write('排名,名称,评分,简介\n')
            for m in movies_list:
                dict_file.write('%s,%s,%s,%s\n' % (m[0], m[1], m[2], m[3]))
    except IOError as ioerr:
        print("文件无法创建，请检查数据文件位置。")

def run(soup):
    list = soup.find(class_='grid_view').find_all('li')
    for item in list:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        if (item.find(class_='inq') != None):
            item_intr = item.find(class_='inq').string
        else: item_intr = ''

        movies_list.append([int(item_index), item_name, item_score, item_intr])


def main(page, list):
    
    url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    run(soup)



def run():

    movies_list = []
    start_time = time.time()
    t = []

    for i in range(0, 10):
        t.append(Thread(target=main, args=(i, movies_list)))
    for j in t:
        j.setDaemon(True)
        j.start()
    for j in t:
        j.join()

    over_time = time.time()
    print(f'总共运行时间：{over_time - start_time:.2f} s')
    save_file(movies_list.sort())
    print('文件已保存')