# 服务器配置
HOST = '192.168.2.8'
PORT = 5858
PORT1 = 5859

# 数据库连接配置
db_config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'sensor_data',
}

'''
# 初始化DS18B20设备
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
'''