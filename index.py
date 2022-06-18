import json, os, sched, time
from abc import ABC, abstractmethod


# for device in devices: 
#     device_dir = devices_dir+'/'+device 
#     with open (device_dir) as file:
#         data = json.load(file)
#         if(data["device_state"] == 'normal'):
#             print(data['device_name'],'Conectado')
#         else:
#             print('Alerta! Dispositivo',data['device_name'])

class Device: 
    def __init__(self, id_device, device_name, device_status):
        self.__id_device = id_device
        self.__device_name = device_name
        self.__device_status = device_status
    @property
    def id_device(self):
        return self.__id_device

    @property
    def device_name(self):
        return self.__device_name
    @property
    def device_status(self):
        return self.__device_status

devices_dir = './devices/'

with os.scandir(devices_dir) as files:
        files = [device.name for device in files if device.is_file and device.name.endswith('.json')]

def check_status(status, device):
    if(status == 'Conectado'):
        time.sleep(10)
        print(device, status)
    else: 
        print('Alert', device, status)

def read_json():
    device_list = []
    for device in files: 
        device_dir = devices_dir+'/'+device
        with open (device_dir) as file:
            try: 
                data = json.load(file)
                device = Device(data['id_device'],data['device_name'],data['device_status'])
                device_list.append(device)
                check_status(device.device_status, device.device_name)
                # print(device_list)
            except:
                print('Dispositivo no tiene información')
                raise
    return device_list

def listen_devices(seconds):
    read_json()
    time.sleep(seconds)



# s = sched.scheduler(time.time, time.sleep)

# def system_state (sc):
#     print("Dispositivo conectado")
#     sc.enter(5, 1, system_state,(sc,))
# s.enter(5,1,system_state, (s,))
# s.run()

while True:
    listen_devices(1)
