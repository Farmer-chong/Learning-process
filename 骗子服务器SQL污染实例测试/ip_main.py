import requests
from bs4 import BeautifulSoup
# 爬取https://www.xicidaili.com/wt 的IP以及端口号
# 并将爬取到的ip和port放入ip_list字典里
def Get_iplist():
    url='https://www.xicidaili.com/wt'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    user_header = {'User-agent': user_agent}
    response = requests.get(url, headers = user_header)
    soup = BeautifulSoup(response.content,'html.parser')
    table = soup.find_all('tr', class_="odd")
    ip_list = []
    for data in table:
       ip = data.contents[3].text
       port = data.contents[5].text
       ip_list.append({
           'ip':ip,
           'port': port
       })
    return ip_list

# print(Get_iplist()[1])
