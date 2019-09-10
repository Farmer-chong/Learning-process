import urllib
import random
import string
import requests

user_agent = '填写抓到的user-agent'
Referer = '填写抓到的referer'
user_header = {'User-agent': user_agent, 'Referer': Referer}
# 随机定义注入的用户名和密码
user_name = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q'
                                ,'p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))  
passwd = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q'
                                ,'p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'
                                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 9))
# 提交的表单内容
url_post = {
    'handle':'reg',
    'usr':user_name,
    'pwd':passwd
}
url = '填写目标URL'
r = requests.post(url, data = url_post, headers = user_header) # 将表单提交到目标URL 
# 显示提交信息
print("POST: " + url +'\n' + "  UserName: " + user_name  + "  PassWd: " + passwd )
print("响应时间：" + str(r.elapsed.total_seconds()) + str(r.status_code))