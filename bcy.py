import re
import urllib.request
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)
url = input('please input BCY url:')
# driver = webdriver.Chrome()
# driver.get(url)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
web = urllib.request.Request(url,headers=headers)
page = urllib.request.urlopen(web)
soup = BeautifulSoup(page,'lxml')

time.sleep(5)
# soup = BeautifulSoup(driver.page_source,'lxml')
# print(driver.page_source)
soup_find = soup.find_all('img',class_='detail_std')
for get_link in soup_find:
    img_src = get_link.get('src')
    re_img_src = re.findall(r'(.*.jpg)',img_src)
    file_name = re.findall('r.*/(.*.jpg)',img_src)
    urllib.request.urlretrieve(re_img_src[0],file_name[0])
    time.sleep(5)

# driver.close()
