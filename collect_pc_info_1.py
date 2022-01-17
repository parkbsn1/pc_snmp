import wmi

WMI_OBJ = wmi.WMI()

process_list = WMI_OBJ.Win32_Process()
print(len(process_list))
print(type(process_list))

# process_name = [process.Name for process in process_list]
# process_name.sort()
cnt = 0
for process in process_list:

    if not (str(process.Name)).startswith('Shell'):
        continue
    cnt += 1
    print(type(process))
    print(process.Caption)
    print(process)
    # print(process)

    if cnt > 3:
        break

