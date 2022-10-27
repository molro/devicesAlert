<h1 align="center">Ejercicio 👋</h1>

> Ejericio resuelto para Ctelec
> 
## Generalidades
**Versión Utilizada**  
- Python 3.10.4

**Librerias Utilizadas**  
- os, time, abc y json

## Estructura General
- [Ver Requisitos](https://github.com/molro/devicesAlert/blob/main/requisitos.md)
- ``\devices`` -> Directorio donde se alojarán los dipositivos.  
- ``\phones``-> Directorio donde se alojarán los "Teléfonos".  

### Plantillas
**Dispositivos**
- ``\devices\device_template.json`` -> Archivo para simular los dispositivos:
    - "id_device": String -> "dev01", referencia: Id del teléfono asignado de contacto    
    - "device_name": String -> "Dispositivo 1", referencia: Nombre del dispositivo
    - "device_status": String -> "Conectado", referencia: Por defecto, Conectado y representa el estado funcional  
    - "emergency_phone": String -> "Phone03", referencia: Id del teléfono asignado de contacto   

**Teléfonos**
- ``\phone\phone_template.json`` -> Archivo para simular los teléfonos:
    - "id_phone": String -> "Phone 01", referencia: Id del teléfono asignado de contacto    
    - "phone": Int  ->  662233123, referencia: Número el cúal se asigna a los dispositivos
 
**Ejecutar Script**  
``python3 index.py`` -> Inicia el script

## Authors

👤 **Mauricio**

- Github: [@molro](https://github.com/molro)

## Dame tu apoyo

Una ⭐️ si te ha gustado y/o ayudado

---
