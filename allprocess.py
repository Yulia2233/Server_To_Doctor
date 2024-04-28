from client_connection import *
import socket
import threading
from setting import *




def start_server_tempature(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"服务器启动，监听 {host}:{port}")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"连接地址: {addr}")
        # 为每个客户端连接创建一个新线程
        client_thread = threading.Thread(target=handle_client_connection_temperature, args=(client_socket,))
        client_thread.start()


def start_server_blood_pressure(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"服务器启动，监听 {host}:{port}")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"连接地址: {addr}")
        # 为每个客户端连接创建一个新线程
        client_thread = threading.Thread(target=handle_client_connection_blood_pressure, args=(client_socket,))
        client_thread.start()