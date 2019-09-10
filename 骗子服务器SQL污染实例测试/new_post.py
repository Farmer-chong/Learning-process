import random
import string
import requests
import time
import ip_main

user_agent = '2333333'
Referer = 'https://********/sign_up.html'
user_header = {'User-agent': user_agent, 'Referer': Referer, 'Cookie': '*****'}
# 获取爬虫代理IP
def prox_ip(ip_list):
        ip_text = ip_list[random.randint(0,len(ip_list))]
        ip = ip_text['ip'] + ':' + ip_text['port']
        proxy = {"http": str(ip)}
        return proxy
# 取随机字符串
def ran_num(get_num):
        num = ''.join(random.sample(['!','@','#','$','<','>','.','?','/','(','%','*',')','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], get_num))
        return num
def main():
        ip_list = ip_main.Get_iplist()
        url_post_data = {
                'operate': 'reg',
                'user': ran_num(6),
                'passwd': ran_num(9)

        }
        url = "https://********/php/api.php"
        r = requests.post(url, data = url_post_data, headers = user_header, proxies = prox_ip(ip_list))
        print("POST: " + url + '\n' + "UserName: " + url_post_data['user']  + "  PassWd: " + url_post_data['passwd'] )
        print("响应时间：" + str(r.elapsed.total_seconds()) + str(r.status_code))
        print("代理IP为:" + str(prox_ip(ip_list)))
        # 如果失败，打印网页信息
        if len(r.text) < 20:
                print(r.text)
# 死循环
while True:
        main()
        time.sleep(1)
