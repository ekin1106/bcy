import re
# import urllib.request
import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import time
import wget
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)

# driver = webdriver.Chrome()
# driver.get(url)
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# web = urllib.request.Request(url,headers=headers)
# page = urllib.request.urlopen(web)
def bcy_page(url):
    web = requests.session()
    cos_page = web.get(url)
    cos_page.encoding = 'utf-8'
    soup = BeautifulSoup(cos_page.text,'lxml')
    time.sleep(3)
    soup_find = soup.find_all('img',{'class':'detail_clickable'})#detail_std')
    download_links = []
    for get_link in soup_find:
        img_src = get_link.get('src')
        re_img_src = re.findall(r'(.*.jpg)',img_src)
        file_name = re.findall('r.*/(.*.jpg)',img_src)
        download_links.append(re_img_src[0])
    return download_links
    #     urllib.request.urlretrieve(re_img_src[0],file_name[0])
    #     time.sleep(5)

def down_pic(link):
    '''wget模块下载'''
    wget.download(link)

if __name__ == '__main__':
    url = input('please input BCY url:')
    link = bcy_page(url)
    pool = ThreadPool(5)
    pool.map(down_pic,link)
    pool.close()
    pool.join()
