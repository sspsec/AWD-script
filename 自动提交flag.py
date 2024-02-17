import requests
import time
import json

session = requests.Session()
with open("key.txt", "r") as f:
    for key in f.readlines():
        paramsPost = {"answer": key.replace("\n", "")}
        headers = {"Origin": "http://172.17.120.6", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
                   "Referer": "http://172.17.120.6/", "Connection": "close", "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                   "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        cookies = {"PHPSESSID": "p965qtvq1ireq3l4dk058qeha0"}
        response = session.post("http://172.17.120.6/Title/TitleView/savecomprecord", data=paramsPost, headers=headers,
                                cookies=cookies)
        
        time.sleep(2)
        print(json.loads(response.text)["msg"])
