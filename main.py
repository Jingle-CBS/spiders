import csv

import requests


url = 'https://api.bilibili.com/x/player/pagelist?bvid=BV1FV41177a6&jsonp=jsonp'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
resp = requests.get(url, headers=headers, verify=False)
dic = resp.json()
#print(dic)
for it in dic['data']:
    print(str(it['page'])+'.'+it['part']+' '+str(it['duration']))