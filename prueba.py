class Clase: 
    def __init__(self, nombre):
        self.__nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre

clase1 = Clase('Clases')

print(clase1.nombre)

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

device01 = Device('dev01', 'Dispositivo 1', 'normal')
print(device01)