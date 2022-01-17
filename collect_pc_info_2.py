import psutil
import numpy as np
#https://npd-58.tistory.com/27


def Get_CPU_INFO():
    # @ Todo CPU 정보
    print('-'*30)
    print(f"CPU info")
    print(f"CPU Physical cnt: {psutil.cpu_count(logical=False)}")
    print(f"CPU Logical cnt: {psutil.cpu_count(logical=True)}")
    cpu_logical_used_percent = np.array(psutil.cpu_percent(interval=0.5,percpu=True))
    print(f"CPU_Logical used percent: {cpu_logical_used_percent}")
    print(f"CPU_Logical used percent(AVG): {np.mean(cpu_logical_used_percent)}")

    #return할 정보만 설정

def GET_Mem_INFO():
    # @ Todo Memory 정보
    print('-'*30)
    print(f"Memory info")
    print(f"Mem: {psutil.virtual_memory()}")
    print(f"Mem_total: {psutil.virtual_memory().total/1024/1024/1024}GB")
    print(f"Mem_Total_percent: {psutil.virtual_memory().percent}")
    print(f"Mem_available_percent: {psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}")
    memory_info_dict = dict(psutil.virtual_memory()._asdict())
    #memory_info_dict 형태 -> {'total': 17042952192, 'available': 4063154176, 'percent': 76.2, 'used': 12979798016, 'free': 4063154176}
    print(f"test_dict: {memory_info_dict}")

    # return할 정보만 설정

def GET_DISK_INFO():
    # @ Todo Disk 정보
    print("-"*30)
    print(f"Disk info")
    disk_partitions = psutil.disk_partitions(all=False)

    disk_used_info_dict = {}
    for disk_partition in disk_partitions:
        disk_used_info_dict[disk_partition[0]] = psutil.disk_usage(disk_partition[1])

    for k, v in disk_used_info_dict.items():
        print(f"partition: {k} | percent: {v.percent} | detail: {v} ")

    # return할 정보만 설정

def GET_Network_INFO():
    # @ Todo Network 정보
    print('-' * 30)
    print(f"Network info")

    #netstate정보
    # netstat_info = psutil.net_connections(kind='inet')
    # print(f"type: {type(netstat_info)} | len: {len(netstat_info)}")
    # for net_info in netstat_info[:3]:
    #     print(f"{net_info}")

    #net_if 정보
    net_if_info = psutil.net_if_addrs()
    print(f"type: {type(net_if_info)} | len: {len(net_if_info)}")
    net_info_dict = {}
    for k, v in net_if_info.items():
        tmp_dict={}
        tmp_dict['mac'] = v[0].address
        tmp_dict['ip'] = v[1].address
        tmp_dict['netmask'] = v[1].netmask
        # if k == 'Wi-Fi':
        # print(f"{k} \t {v}")
        # print(f"MAC: {v[0].address}")
        # print(f"IP: {v[1].address}")
        # print(f"netmask: {v[1].netmask}")
        net_info_dict[k] = tmp_dict
    print(net_info_dict)

def GET_Process_INFO():
    # for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
    #     print(proc.info)

    procs_list_1 = [proc.info for proc in psutil.process_iter(attrs=['pid', 'name', 'username'])]
    print(f"list 형식 출력({len(procs_list_1)})")
    print(procs_list_1)

    procs_dict_1 = {p.pid: p.info for p in psutil.process_iter(attrs=['name', 'username'])}
    print(f"dict 형식 출력({len(procs_dict_1)})")
    print(procs_dict_1)
    #key=PID, value={'username': 사용자명, 'name': 프로세스 이름}

    procs_name_list_1 = [proc.name() for proc in psutil.process_iter(attrs=['name'])]
    print(f"procs name list 출력({len(procs_name_list_1)})")
    print(procs_name_list_1)
    unique_proc_name = list(set(procs_name_list_1))
    print(f"procs name 중복제거({len(unique_proc_name)})")
    print(unique_proc_name)
    # print(procs_name_dict_1.values())


def TEST_INFO():
    # @ Todo Process 정보
    print('-'*30)
    print(f"Process info")
    process_dict = {process.name:str(process.pid) for process in psutil.process_iter()}
    for process in psutil.process_iter():
        print(process)
        pass
        break

    print('-'*30)
    cnt = 0
    process_dict ={}
    for process in psutil.process_iter():
        print(process)
        tmp_dict = {}
        tmp_dict['pid'] = str(process.pid)
        tmp_dict['name'] = process.name()
        tmp_dict['status'] = process.status()
        tmp_dict['cpu_percent'] = process.cpu_percent()
        tmp_dict['memory_percent'] = process.memory_percent()*100
        tmp_dict['memory_info'] = process.memory_info
        tmp_dict['memory_info_ex'] = process.memory_info_ex

        # tmp_dict['memory_maps'] = process.memory_maps()
        # tmp_dict['memory_full_info'] = process.memory_full_info()
        process_dict[str(process.pid)] = tmp_dict

        cnt += 1
        if cnt > 5:
            break
    #     print(f"{cnt} {process.name()} \t {str(process.pid)}")
    #     cnt +=1
    #     #print(process.name() + "\t"+str(process.pid))

    print('-'*30)
    for k,v in process_dict.items():
        print(k, v)

def main():
    print("Main Function")
    GET_Process_INFO()

if __name__ == "__main__":
    print("Start")
    main()