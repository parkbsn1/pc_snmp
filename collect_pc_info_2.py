import psutil
import datetime
from uptime import uptime
import wmi
import ctypes
import numpy as np
import socket
import getmac
#https://npd-58.tistory.com/27


def Get_CPU_INFO(flag=None):
    #TODO CPU 정보
    result = {}
    result['cpu_used'] = psutil.cpu_percent()
    result['cpu_freq'] = str(round(psutil.cpu_freq().current/1024,2))+'Ghz'

    if flag == 'all':
        print(f"CPU Physical cnt: {psutil.cpu_count(logical=False)}")
        print(f"CPU Logical cnt: {psutil.cpu_count(logical=True)}")
        cpu_logical_used_percent = np.array(psutil.cpu_percent(interval=0.5,percpu=True))
        print(f"CPU_Logical used percent: {cpu_logical_used_percent}")
        print(f"CPU_Logical used percent(AVG): {psutil.cpu_percent()}")
        print(f"CPU freq: {psutil.cpu_freq().current/1024} Ghz")
    return result

def GET_Mem_INFO(flag=None):
    # @ Todo Memory 정보
    result = {}
    result['mem_used'] = psutil.virtual_memory().percent
    result['mem_total'] = str(round(psutil.virtual_memory().total/1024/1024/1024,2))+'GB'

    if flag == 'all':
        print(f"Mem: {psutil.virtual_memory()}")
        print(f"Mem_total: {psutil.virtual_memory().total/1024/1024/1024}GB")
        print(f"Mem_Total_percent: {psutil.virtual_memory().percent}")
        print(f"Mem_available_percent: {psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}")
        memory_info_dict = dict(psutil.virtual_memory()._asdict())
        #memory_info_dict 형태 -> {'total': 17042952192, 'available': 4063154176, 'percent': 76.2, 'used': 12979798016, 'free': 4063154176}
        print(f"test_dict: {memory_info_dict}")

    return result

def GET_DISK_INFO(flag=None):
    # @ Todo Disk 정보
    result = {}
    disk_partitions = psutil.disk_partitions(all=False)

    disk_used_info_dict = {}
    disk_used = []
    disk_total = []
    for disk_partition in disk_partitions:
        disk_used_info_dict[disk_partition[0]] = psutil.disk_usage(disk_partition[1])
        partition_name = disk_partition[0].replace('\\', '')
        used_value = psutil.disk_usage(disk_partition[1]).percent
        total_value = str(round((psutil.disk_usage(disk_partition[1]).total)/1024/1024/1024,2))+'GB'
        disk_used.append({partition_name: used_value})
        disk_total.append({partition_name: total_value})

    if flag == 'all':
        for k, v in disk_used_info_dict.items():
            print(f"partition: {k} | percent: {v.percent} | detail: {v} ")
    result['disk_used'] = disk_used
    result['disk_total'] = disk_total
    # result = {'disk_used': disk_used}

    return result

def GET_DISK_INFO2(flag=None):
    result = {}
    disk_partitions = psutil.disk_partitions(all=False)
    result['disk_used'] = psutil.disk_usage(disk_partitions[0][1]).percent

    return result


def GET_Network_INFO(flag=None):
    # @ Todo Network 정보
    #net_if 정보(전체 수집)
    net_if_info = psutil.net_if_addrs()
    net_info_dict = {}
    for k, v in net_if_info.items():
        print(f"key: {k} | value: {v}")
        tmp_dict={}
        tmp_dict['mac'] = v[0].address
        tmp_dict['ip'] = v[1].address
        tmp_dict['netmask'] = v[1].netmask
        net_info_dict[k] = tmp_dict

    if 'Wi-Fi' in net_info_dict.keys():
        result = net_info_dict['Wi-Fi']
        print('Wi_Fi')
    elif '이더넷 2' in net_info_dict.keys():
        result = net_info_dict['이더넷 2']
        print('이더넷 2')
    elif '이더넷' in net_info_dict.keys():
        result = net_info_dict['이더넷']
        print('이더넷')
    else:
        result = {'mac': '::1', 'ip': '127.0.0.1', 'netmask': '255.255.255.0'} #loopback주소
        print('loopback')

    # print(result)
    #result 형태(dict)예시: {'mac': '8C-55-4A-9C-2E-35', 'ip': '192.168.0.61', 'netmask': '255.255.255.0'}
    return result

def GET_Network_INFO_2(flag=None):
    result = {}

    result['host_name'] = socket.gethostname()
    result['host_ip'] = socket.gethostbyname(socket.gethostname())
    result['host_mac'] = getmac.get_mac_address()

    print(f"nw_2: {result}")
    return result

def GET_Process_INFO(flag=None):
    result = {}
    procs_list_pid = [proc.info for proc in psutil.process_iter(attrs=['pid', 'name', 'username'])]
    result['process_cnt'] = len(procs_list_pid)

    procs_name_list = [proc.name() for proc in psutil.process_iter(attrs=['name'])]
    unique_proc_name = list(set(procs_name_list))
    unique_proc_name = [p_n for p_n in unique_proc_name if p_n !=''] #공백인 process는 제거

    process_name_str = '|'.join(unique_proc_name)
    result['process_name'] = process_name_str
    # result['process_name'] = unique_proc_name

    if flag == 'all':
        print(f"procs name 중복제거({len(unique_proc_name)})")
        print(unique_proc_name)


        procs_list_1 = [proc.info for proc in psutil.process_iter(attrs=['pid', 'name', 'username'])]
        print(f"list 형식 출력({len(procs_list_1)})")
        print(procs_list_1)

        # procs_list_2 = [proc.info for proc in psutil.process_iter(attrs=['pid', 'name', 'username', 'status', 'started'])]
        # print(f"list 형식 출력2({len(procs_list_2)})")
        # print(procs_list_2)

        procs_dict_1 = {p.pid: p.info for p in psutil.process_iter(attrs=['name', 'username'])}
        print(f"dict 형식 출력({len(procs_dict_1)})")
        print(procs_dict_1)
        #key=PID, value={'username': 사용자명, 'name': 프로세스 이름}

    return result

def GET_PC_UPTIME(flag=None):
    # getting the library in which GetTickCount64() resides
    lib = ctypes.windll.kernel32

    # calling the function and storing the return value
    t = lib.GetTickCount64()

    # since the time is in milliseconds i.e. 1000 * seconds
    # therefore truncating the value
    t = int(str(t)[:-3])

    # t = int(str(t))

    # extracting hours, minutes, seconds & days from t
    # variable (which stores total time in seconds)
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)

    # formatting the time in readable form
    # (format = x days, HH:MM:SS)
    print(f"{days} days, {hour:02}:{mins:02}:{sec:02}")



def GET_Battery_INFO(flag=None):
    result = {}
    battery = psutil.sensors_battery()
    result['battery_used'] = battery.percent
    result['power_plugged'] = battery.power_plugged

    if flag == 'all':
        print(f"battery info: {battery}")
        print(f"percent: {battery.percent}%")
        print(f"power_plugged: {battery.power_plugged}")
    return result

def GET_BOOT_TIME(flag=None):
    result = {}
    b_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    n_time = datetime.datetime.now()
    u_time = n_time - b_time

    if flag == 'all':
        print(f"boot_time: {b_time} | now_time: {n_time} | up_time: {u_time} / {type(u_time)}")
        boot_time_str = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        print(f"boot time: {boot_time_str}")

    result['boot_time'] = b_time.strftime("%Y-%m-%d %H:%M:%S")
    result['up_time'] = str(u_time).split('.')[0]

    return result


def main():
    result_dict = {}

    result_dict['network'] = GET_Network_INFO()
    # result_dict['uptime'] = GET_BOOT_TIME()
    # result_dict['battery'] = GET_Battery_INFO()
    # result_dict['disk_2'] = GET_DISK_INFO2()
    # result_dict['network_2'] = GET_Network_INFO_2()

    for k, v in result_dict.items():
        print(f"{k} \t| {v}")

    #GET_PC_UPTIME()
    # GET_BOOT_TIME2()
    # GET_BOOT_TIME3()
    # TEST_INFO()
    # TEST_INFO_2()
    # TEST_INFO_3()



if __name__ == "__main__":
    main()