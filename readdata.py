

def read_exa():
    exam = 12
    return exam


'''
def read_temp_raw():
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines


def read_temp():
    lines = read_temp_raw()
    while 'YES' not in lines[0].strip():
        sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
'''