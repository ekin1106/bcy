# bcy
半次元图片下载
# 测试地址
`` https://bcy.net/coser/detail/30744/2384864 ``
 # 只要复制进项目里就可以下载了
 如果不能下载，则可能是需要关注以后才能看的图
  
 ### 新增一个下载需要用到的软件 https://eternallybored.org/misc/wget/
 
 # UPDATE
 ## 请使用main.py
 bcy改变了html结构，不过内容还是在页面文件里
搜索字段
<script>
    window.__ssr_data = JSON.parse("{\"detail\":{\"currentStyle\":{\"bgColor\":\"white\",\"fontSize\":\"m\",\"indent\":\"noindent\"},\"post_data\":{\"item_id\":\"6323546625541168910\",\"uid\":25434,\"ctime\":1472286631,\"type\":\"note\",\"title\":\"\",\"summary\":\"\",\"content\":\"\",\"plain\":\"初音未来 cn: 桜桃喵\\u003Cbr\\u002F\\u003E摄影：西瓜汪 | 化妆：桜桃喵 | 后期：西瓜汪\",\"word_count\":0,\"multi\":[{\"path\":\"https:\\u002F\\u002Fimg5.bcyimg.com\\u002Fcoser\\u002F10081\\u002Fpost\\u002F1786z\\u002Ff21d39106c2511e6b86d9fa...(line truncated)...
    window._UID_ = '809443'
  </script>
  图片文件在js字段里，提取完以后，  \\u002F  替换/
  \" 替换"
  就可以提取了
