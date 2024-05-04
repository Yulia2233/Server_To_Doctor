import multiprocessing as mlp
from allprocess import *
from setting import *


if __name__ == '__main__':
    temperature_process = mlp.Process(target=start_server_tempature, args=(HOST, PORT,))
    blood_pressure_process = mlp.Process(target=start_server_blood_pressure, args=(HOST, PORT1,))
    temperature_process.start()
    print('测温连接成功')
    blood_pressure_process.start()
    print('测血压连接成功')