from time import sleep
import mysql.connector
from readdata import *
from setting import *
def handle_client_connection_blood_pressure(client_socket):
    db_conn = None
    cursor = None
    try:
        db_conn = mysql.connector.connect(**db_config)
        cursor = db_conn.cursor()
        print("新客户端连接")
        message = '请你使用机器的血压器' + "\r\n"
        client_socket.send(message.encode('utf-8'))
        while True:
            message = read_exa()
            print(f"血压: {message} ")
            cursor.execute("INSERT INTO data_logs (blood_pressure) VALUES (%s)", (message,))
            db_conn.commit()
            message = str(message) + '\r\n'
            client_socket.send(message.encode('utf-8'))
            sleep(5)  # 每5秒读取并上传一次数据
    except mysql.connector.Error as err:
        print("Database connection failed:", err)
    finally:
        client_socket.close()
    if cursor is not None:
        cursor.close()
    if db_conn is not None:
        db_conn.close()


def handle_client_connection_temperature(client_socket):
    db_conn = None
    cursor = None
    try:
        db_conn = mysql.connector.connect(**db_config)
        cursor = db_conn.cursor()
        print("新客户端连接")
        message = '请你使用机器的体温计' + "\r\n"
        client_socket.send(message.encode('utf-8'))

        while True:
            # 读取单片机，数据
            message = read_exa()
            print(f"现在温度: {message} °C")
            # 加入数据库中
            cursor.execute("INSERT INTO data_logs (temperature) VALUES (%s)", (message,))
            db_conn.commit()
            # 发送到客户端
            message = str(message) + '\r\n'
            client_socket.send(message.encode('utf-8'))
            sleep(5)  # 每5秒读取并上传一次数据
    except mysql.connector.Error as err:
        print("Database connection failed:", err)
    finally:
        client_socket.close()
    if cursor is not None:
        cursor.close()
    if db_conn is not None:
        db_conn.close()