import requests

session = requests.Session()

with open("flag.txt", "r") as f:
    flags = f.readlines()
    for flag in flags:
        print(flag)
        paramsGet = {"event_id": "21"}
        rawBody = {"flag": flag.replace("\n", ""), "token": "tUnum26J4s8gc8mfRQC7VeHNfdGJJajWQWMMSTtq6tWDc"}
        headers = {"Origin": "http://10.10.10.10", "Accept": "application/json, text/plain, */*",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
                   "Referer": "http://10.10.10.10/", "Connection": "close",
                   "X-CSRF-Token": "Ijk3YTM4NzNjYWEyNzMyM2Y5ZGEzY2E5YjJiZmRmYzI2NTBkMTNlYWQi.YM1BGQ.Ieqg5M54FH5h-Cye-c7ZIYRBmIM",
                   "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                   "Content-Type": "application/json;charset=UTF-8"}
        cookies = {"xid": "team65",
                   "X-CSRF-Token": "Ijk3YTM4NzNjYWEyNzMyM2Y5ZGEzY2E5YjJiZmRmYzI2NTBkMTNlYWQi.YM1BGQ.Ieqg5M54FH5h-Cye-c7ZIYRBmIM",
                   "session": "1cc3ea91-c452-47c6-b655-d52c0b485679"}
        response = session.post("http://10.10.10.10/api/v1/att_def/web/api/submit_flag/", json=rawBody,
                                params=paramsGet,
                                headers=headers, cookies=cookies)
        print(response.text)