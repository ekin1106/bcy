from requests_html import HTMLSession
import json
import requests
import re
import wget
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

class bcy():
    def CoserPage(self,uid):
        url = 'https://bcy.net/u/{}'.format(uid)
        session = HTMLSession()
        r = session.get(url)
        r.html.render()
        CoserItem = r.html.find('.l-newTimelineItem', first=False)
        first = CoserItem[0].attrs['data-item-id']
        print(first)
        jsonURL = 'https://bcy.net/home/timeline/loaduserposts?since={0}&grid_type=timeline&uid={1}&limit=20'.format(first,uid)
        req = requests.session()
        web = req.get(jsonURL).json()
        data = web['data']
        ID = []
        ID.append('https://bcy.net/item/detail/{}'.format(first))
        '''获取所有的作品编号，当json里data的数量为0则为最后一页'''
        while(len(data) != 0 ):
            for IdNum in data:
                ID.append('https://bcy.net/item/detail/{}'.format(IdNum['since']))

            lastID = data[-1]['since']
            jsonURL = 'https://bcy.net/home/timeline/loaduserposts?since={0}&grid_type=timeline&uid={1}&limit=20'.format(
                lastID, uid)
            web = req.get(jsonURL).json()
            data = web['data']
        print(ID)
        return ID

    def bcy_page(self,url):
        session = HTMLSession()
        r = session.get(url)
        # print(r.text)
        pic = r.html.find('script', first=False)
        for i in pic:
            if i.text.startswith('window.__ssr_data'):
                parse = i.text.split(');')[0].strip('window.__ssr_data = JSON.parse("').strip('")')
                jsonData = parse.replace(r'\"',r'"').replace(r'\\u002F','/')
                j = json.loads(jsonData)['detail']['post_data']['multi']
                download_links =[]
                for u in j:
                    pic_url = u['path'].strip('/w650')
                    print(pic_url)
                    download_links.append(pic_url)
                    
        session.close()
        return download_links

    def down_pic(self,link):
        '''wget模块下载'''
        wget.download(link)

    def test_page(self,url):
        session = HTMLSession()
        r = session.get(url)
        # print(r.text)
        pic = r.html.find('script', first=False)
        for i in pic:
            if i.text.startswith('window.__ssr_data'):
                parse = i.text.split(');')[0].strip('window.__ssr_data = JSON.parse("').strip('")')
                print(parse)
                jsonData = parse.replace(r'\"',r'"').replace(r'\\u002F','/')
                j = json.loads(jsonData)['detail']['post_data']['multi']
                download_links =[]
                for u in j:
                    pic_url = u['path'].strip('/w650')
                    print(pic_url)


if __name__ == '__main__':
    print('''1. 爬取coser所有的图片
    2.爬取单独的图片''')
    Select = input('请输入编号:')
    bcys = bcy()
    if Select == '1':
        # uid = input("please input COSER UID: ")
        uid = '2656350'
        bcys.CoserPage(uid)
    elif Select == '2':
        url = input('please input BCY url:')
        link = bcys.bcy_page(url)
        pool = ThreadPool(5)
        pool.map(bcys.down_pic,link)
        pool.close()
        pool.join()
    elif Select == '3':
        url = 'https://bcy.net/item/detail/6323546625541168910'
        url_1='https://bcy.net/item/detail/6532705667755540749'
        bcys.test_page(url_1)

