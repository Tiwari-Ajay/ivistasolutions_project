"""
import socket
import sys
import datetime
import pynput
import time
import threading
def server_communication():
    try:
        server_stop = False
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_no = 2001
        server_socket.bind(('0.0.0.0', port_no))
        server_socket.listen(5)
        print('Server Started')
        print('server listening from ...', datetime.datetime.now())
        # SET text in status box
        # self.status_textarea.insert(INSERT,'Server Started')
        while True and not server_stop:
            conn, addr = server_socket.accept()
            from_client = ''
            while True and not server_stop:
                data = conn.recv(4096)

                if (not data): break
                from_client += data.decode('utf8')
                print(from_client + ' Port ' + str(port_no) + ' Time: ' + str(datetime.datetime.now()))
                time.sleep(0.1)
                # conn.send("received".encode())
                # handle_termination()
            conn.close()
        print('server disconnected and shutdown')
    except Exception as e:
        temp=e
        temp= str(temp).split(' ')
        #print(temp)
        print(f'{"Port "+ str(port_no)+" "+" ".join(temp[3:])}:Connection Terminated')

server_communication()
"""

# import threading
import socket
from _thread import *
import datetime
import threading
import time
"""
# Define required parameters :
PORT = 5050
# dynamicly get your ip :
HOST = socket.gethostbyname(socket.gethostname())  # 192.168.0.110
FORMAT = 'utf-8'
HEADER = 1024  # Buffer size
ADDR = (HOST, PORT)
# print_lock = threading.Lock()

# Define socket type TCP , using Addressing protocol:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


# Receive data from client :
# socket not send plain text thats why using utf-8 encode string :
# Header : use to get msg with same buffer size as client msg buffer use :
# if succefully get data then send confirmation to the client :
def ClientHandler(connection):
    connected = True
    while connected:
        data = connection.recv(HEADER)
        if not data:
            # print_lock.release()
            print('bye')
            break;
        print(str(data.decode(FORMAT)))
        connection.send('message_send'.encode(FORMAT))

    connection.close()


# 1. Listen incomming connection:
# 2. Accept all connection :
# 3. Create Client Thread :
# 4. Close the connection :
def Start():
    server.listen()
    listining = True
    while listining:
        conn, addr = server.accept()
        print(f'[CONNECTED]-> {addr}')
        # print_lock.acquire()
        start_new_thread(ClientHandler, (conn,))
    server.close()


print('****[ SERVER STARTING ]****')
Start()

"""

server=None #global for all method
server_stop=False #stop the server
def clientHandler(connection):
    connected = True
    while connected:
        data = connection.recv(4048)
        if not data:
            print('No Data')
            break;
        print(str(data.decode('utf-8')))
    connection.close()
def server_communication():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0',5050))
    server.listen(4048)
    global server_stop
    server_stop= False
    while not server_stop:
        conn, addr = server.accept()
        print(f'[CONNECTED]-> {addr}')
        start_new_thread(clientHandler, (conn,))
    server.close()

print('****[ SERVER STARTING ]****')
server_communication()
