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
                parse = i.text.split(';')[0].strip('window.__ssr_data = JSON.parse("').strip('")')
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
                parse = i.text.split(';')[0].strip('window.__ssr_data = JSON.parse("').strip('")')
                jsonData = parse.replace(r'\"',r'"').replace(r'\\u002F','/')
                j = json.loads(jsonData)['detail']['post_data']['multi']
                download_links =[]
                for u in j:
                    pic_url = u['path'].strip('/w650')
                    download_links.append(pic_url)


if __name__ == '__main__':
    print('''1. 爬取coser所有的图片
    2.爬取单独的图片''')
    Select = input('请输入编号:')
    bcy = bcy()
    if Select == '1':
        # uid = input("please input COSER UID: ")
        uid = '2656350'
        bcy.CoserPage(uid)
    elif Select == '2':
        url = input('please input BCY url:')
        link = bcy.bcy_page(url)
        pool = ThreadPool(5)
        pool.map(bcy.down_pic,link)
        pool.close()
        pool.join()
    elif Select == '3':
        url = 'https://bcy.net/item/detail/6323546625541168910'
        bcy.test_page(url)

'''
<script>
    window.__ssr_data = JSON.parse("{\"detail\":{\"currentStyle\":{\"bgColor\":\"white\",\"fontSize\":\"m\",\"indent\":\"noindent\"},\"post_data\":{\"item_id\":\"6323546625541168910\",\"uid\":25434,\"ctime\":1472286631,\"type\":\"note\",\"title\":\"\",\"summary\":\"\",\"content\":\"\",\"plain\":\"初音未来 cn: 桜桃喵\\u003Cbr\\u002F\\u003E摄影：西瓜汪 | 化妆：桜桃喵 | 后期：西瓜汪\",\"word_count\":0,\"multi\":[{\"path\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002Ff21d39106c2511e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445828,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F70d967906c2311e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4441277,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F7b2646a06c2311e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4441306,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F848eb9206c2311e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4441347,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002Fa0afb1306c2411e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4444851,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002Fb8231c306c2411e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4444875,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002Fc084cd106c2411e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4444966,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002Fd6b705806c2411e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445090,\"w\":6000,\"h\":4000},{\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F21ef75f06c2511e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445118,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F48722a106c2511e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445140,\"w\":6000,\"h\":4000},{\"path\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F572e71306c2511e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445162,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F63930cb06c2511e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445183,\"w\":6000,\"h\":4000},{\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F6eddacb06c2511e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445205,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F7ab634d06c2511e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445517,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F8cfd29506c2511e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445573,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F9f8a75a06c2511e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445593,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002Fb1d254806c2511e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445645,\"w\":6000,\"h\":4000},{\"path\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002Fc9258d506c2511e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445686,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002Fdd0486f06c2511e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445762,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F04e9ff606c2611e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445873,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F12b333f06c2611e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445904,\"w\":4000,\"h\":6000},{\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002F2297f5806c2611e6b86d9fabdae62003.jpg\\u002Fw650\",\"type\":\"image\",\"mid\":4445973,\"w\":5396,\"h\":2313}],\"pic_num\":22,\"work\":\"VOCALOID\",\"wid\":3770,\"work_real_name\":\"VOCALOID\",\"post_tags\":[{\"tag_id\":399,\"tag_name\":\"COS\",\"type\":\"tag\",\"cover\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fcore\\u002Ftags\\u002Fflag\\u002F179t0\\u002Fbc35e9d0b98c11e89533e7273e251f0e.png\\u002F2X2\",\"post_count\":371771},{\"tag_id\":15,\"tag_name\":\"古风\",\"type\":\"tag\",\"cover\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcore\\u002Ftags\\u002Fflag\\u002F178ki\\u002F250a6e90088611e79cd2af395e9b927b.png\\u002F2X2\",\"post_count\":150890},{\"tag_id\":35,\"tag_name\":\"miku\",\"type\":\"tag\",\"cover\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fuser\\u002F2718434\\u002Fitem\\u002Fc0joq\\u002Fvvjisfj7aa7gkgglmexzturk1bzvgdph.jpg\\u002F2X2\",\"post_count\":4440},{\"tag_id\":5012,\"tag_name\":\"腿控\",\"type\":\"tag\",\"cover\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcore\\u002Ftags\\u002Fflag\\u002F1789d\\u002F2189c180796611e691a2edfca5299ac1.jpg\\u002F2X2\",\"post_count\":4065},{\"tag_id\":64692,\"tag_name\":\"我要上推荐\",\"type\":\"tag\",\"cover\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fuser\\u002F96455191212\\u002Fitem\\u002Fc0jmj\\u002F7ba1810b66bf410c9f0b9eb4e044aa36.jpg\\u002F2X2\",\"post_count\":35974},{\"tag_id\":4122,\"tag_name\":\"金丝雀\",\"type\":\"tag\",\"cover\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fuser\\u002F1617783\\u002Fitem\\u002Fc0jh2\\u002Fzvrxxyf5s3uchmnd4clfn0jdwcypskbl.jpg\\u002F2X2\",\"post_count\":445},{\"tag_id\":32,\"tag_name\":\"初音未来\",\"type\":\"tag\",\"cover\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Fuser\\u002F1060813\\u002Fitem\\u002Fc0jou\\u002Feftfdqitd4cdxjrl7h8x980aqet5klza.jpg\\u002F2X2\",\"post_count\":25266}],\"like_count\":1783,\"user_liked\":false,\"reply_count\":65,\"share_count\":3,\"editor_status\":\"all_public\",\"forbidden_right_click\":true,\"view_need_login\":false,\"view_need_fans\":false,\"no_trans\":false,\"no_modify\":false,\"postStatus\":\"normal\"},\"detail_user\":{\"uid\":25434,\"avatar\":\"https:\\u002F\\u002Fuser.bcyimg.com\\u002FPublic\\u002FUpload\\u002Favatar\\u002F25434\\u002F28010013d3844d9e9f8cab518dc13717\\u002Ffat.jpg\\u002Fabig\",\"uname\":\"桜桃喵\",\"self_intro\":\"CN桜桃喵，读音是樱桃的桜桃，猫了个喵。来自深圳，你可以选着喜欢我和喜欢我 (=′∇`=） ♥粉丝群：544183156 ｜粉丝2群：700893779(不是粉勿加\",\"sex\":0,\"following\":15,\"follower\":9005,\"followstate\":\"havefollow\",\"value_user\":0,\"show_utags\":true,\"utags\":[{\"ut_id\":1,\"ut_name\":\"Coser\"},{\"ut_id\":2,\"ut_name\":\"绘师\"}]},\"top_lists\":[{\"id\":204071,\"ttype\":\"coser\",\"sub_type\":\"lastday\",\"stime\":20160829,\"rank\":1},{\"id\":204682,\"ttype\":\"coser\",\"sub_type\":\"lastday\",\"stime\":20160830,\"rank\":2},{\"id\":206413,\"ttype\":\"coser\",\"sub_type\":\"week\",\"stime\":20160902,\"rank\":3},{\"id\":207634,\"ttype\":\"coser\",\"sub_type\":\"week\",\"stime\":20160904,\"rank\":4},{\"id\":205804,\"ttype\":\"coser\",\"sub_type\":\"week\",\"stime\":20160901,\"rank\":4},{\"id\":207024,\"ttype\":\"coser\",\"sub_type\":\"week\",\"stime\":20160903,\"rank\":4},{\"id\":205195,\"ttype\":\"coser\",\"sub_type\":\"week\",\"stime\":20160831,\"rank\":5},{\"id\":204591,\"ttype\":\"coser\",\"sub_type\":\"week\",\"stime\":20160830,\"rank\":11},{\"id\":203990,\"ttype\":\"coser\",\"sub_type\":\"week\",\"stime\":20160829,\"rank\":20}],\"detail_banners\":[{\"link\":\"https:\\u002F\\u002Fbcy.net\\u002Fhuodong\\u002F182\",\"path\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Feditor\\u002Fflag\\u002F179q5\\u002Fa6f6d2b09eab11e88a3a1707c988b050.jpg\",\"title\":\"\"},{\"link\":\"https:\\u002F\\u002Fbcy.net\\u002Fhuodong\\u002F192\",\"path\":\"https:\\u002F\\u002Fimg9.bcyimg.com\\u002Feditor\\u002Fflag\\u002F179sw\\u002Fb0f379b0b67711e8a941d53b6054939d.jpg\",\"title\":\"\"}],\"self\":false},\"user\":{\"uid\":\"809443\"}}");
    window._UID_ = '809443'
  </script>

  \\u002F  替换/
  \" 替换"
'''
