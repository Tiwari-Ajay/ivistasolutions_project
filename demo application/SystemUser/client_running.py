import datetime
import time
import socket
import threading
def client_fun(ids_list):
    for i in range(5):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.0.178', 2002))
        #client.send(f"from client 1-{i+1}".encode())
        client.send(ids_list[i].encode())
        time.sleep(0.1)
        #print('from client:',datetime.datetime.now())
ids_list=[]
for i in range(5):
    str1=""
    for j in range(1,11):
        str1=str1+str(j+i*10)
        if j!=10:
            str1 = str1 + ','
    ids_list.append(str1)
#print(ids_list)
client_fun(ids_list)
#send_thread = threading.Thread(target=client_fun)
#from_server = client.recv(4096)
#client.close()
#print (from_server.decode())
'''
# Python code for simple port scanning

import socket  # importing library

ip = socket.gethostbyname(socket.gethostname())  # getting ip-address of host

for port in range(65535):  # check for all available ports

    try:

        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a new socket

        serv.bind((ip, port))  # bind socket with address

    except:

        print('[OPEN] Port open :', port)  # print open port number

    serv.close()  # close connection
'''
'''
from pathlib import Path
path=Path('./log.txt')
if path.is_file():
    with open('log.txt', 'r') as f:
        print(f.readlines())
else:
    print("No such file")
'''
