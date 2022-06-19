from abc import abstractmethod
import json, os, time
## Clase para implementar los dispositivos
class Device: 
    def __init__(self, id_device, device_name, device_status, emergency_phone):
        self.__id_device = id_device
        self.__device_name = device_name
        self.__device_status = device_status
        self.__emergency_phone = emergency_phone
    @property
    @abstractmethod
    @abstractmethod
    def id_device(self):
        return self.__id_device

    @property
    @abstractmethod
    def device_name(self):
        return self.__device_name
    @property
    @abstractmethod
    def device_status(self):
        return self.__device_status
    
    @property
    @abstractmethod
    def emergency_phone(self):
        return self.__emergency_phone
class Phone:
    def __init__(self, id_phone, phone):
        self.__id_phone = id_phone
        self.__phone = phone
    
    @property
    @abstractmethod
    def id_phone(self):
        return self.__id_phone
    
    @property
    @abstractmethod
    def phone(self):
        return self.__phone

devices_dir = './devices/'
phones_dir = './phones/'

with os.scandir(devices_dir) as devices:
        devices = [device.name for device in devices if device.is_file and device.name.endswith('.json')]

with os.scandir(phones_dir) as phones:
        phones = [phone.name for phone in phones if phone.is_file and phone.name.endswith('.json')]

def check_status(devices):
    for device in devices:
        state = { 'Device': device.device_name, 'Status' : device.device_status, 'Emergency Phone': device.emergency_phone}
        if(device.device_status != 'Conectado'):
            print('Alert', state)
        else: 
            print(state)

def check_alert(status, device, phone):
    if(status != 'Conectado'):
        state = { 'Device': device, 'Status' : status, 'Emergency Phone': phone}
        print('Alert -', state)

def read_phone(array, dir):
    phone_list =[]
    for element in array:
        inbox = dir+'/'+element
        with open(inbox) as file:
            try:
                data = json.load(file)
                numeros = list(data.values())
                phone = Phone(numeros[0],numeros[1])
                phone_list.append(phone)
            except:
                print('No hay teléfono')
                raise
    return phone_list

def read_devices(array, dir):
    object_list = [] 
    phone_list = read_phone(phones, phones_dir)
    for element in array:
        inbox = dir+'/'+element
        with open (inbox) as file:
            try: 
                data = json.load(file)
                propiedades = list(data.values())
                for phone in phone_list:
                    if(phone.id_phone == propiedades[3]):
                        emergency_phone = phone.phone
                object = Device(propiedades[0],propiedades[1],propiedades[2], emergency_phone)
                check_alert(object.device_status, object.device_name, object.emergency_phone)
                object_list.append(object)
            except:
                print('Dispositivo no tiene información')
                raise
    return object_list


def listen_devices(seconds):
    read_devices(devices, devices_dir)
    time.sleep(seconds)

time_status = 1 

while True:
    listen_devices(1)
    time_status += 1
    if(time_status % 2 == 0):
        device_to_check = read_devices(devices, devices_dir)
        check_status(device_to_check)