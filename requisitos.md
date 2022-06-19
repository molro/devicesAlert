Te proponemos un ejercicio para la evolución de tu experiencia.  
Consiste en crear el software en Python utilizando las librerías que tú consideres necesarias, con las siguientes características:  

El programa consistirá en un bucle infinito que responderá a diferentes sucesos:  
Cada minuto se mostrará por pantalla el estado del sistema.   
El estado del sistema se define por los siguientes parámetros:  
- Teléfono de contacto asignado.  
- Estado de un primer dispositivo anexo conectado.  
- Estado de un segundo dispositivo anexo conectado.  
Los dos dispositivos conectados serán “imaginarios”, no reales. Supuestamente ambos dispositivos lanzan información en formato de un fichero JSON que será grabado en un directorio del sistema.   Simularemos este mecanismo copiando a mano los ficheros JSON en el directorio. Igualmente, el teléfono de contacto estará descrito en otro fichero JSON que igualmente copiaremos a mano.  
Si los ficheros JSON recibidos anuncian un salto de alarma, el programa deberá detectarlo inmediatamente y mostrar una alarma (por pantalla) sin esperar a que pase el minuto de refresco de estado.  
Siéntete libre de crear tú mismo los ficheros JSON necesarios para indicar la información necesaria.  
En el momento en el que se realice el chequeo cíclico cada minuto o cuando se produzca una alarma, el programa debe mostrar el estado de cada uno de los dos dispositivos y el teléfono de contacto asignado.  
Valoramos especialmente:  
- La claridad del código  
- La eficiencia de los algoritmos  
- Las buenas prácticas  
El uso adecuado de clases y funciones:  
Contempla la posibilidad de que en un futuro se incorporen otros dispositivos u otra información dentro de los JSON.  
Por tanto, valoramos la escalabilidad del código.  