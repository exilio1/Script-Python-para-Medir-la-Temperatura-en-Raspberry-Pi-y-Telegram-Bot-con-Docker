Hola todos.
primero que todo me presento, mi nombre es Cristian Marin,  una persona que apenas esta aprendiendo a programar.
Quiero compartirles este programa.

Sirve para monitorear la temperatura de nuestras Raspberry pi, por medio de un Boot de Telegram.

Script Python para Medir la Temperatura en Raspberry Pi y Telegram Bot con Docker

1. Crear el bot de Telegram
1. Ve a Telegram y busca el bot @BotFather.
2. Crea un nuevo bot y obtén el token de la API.
2. Escribir el script de Python
El script medirá la temperatura de la Raspberry Pi y enviará el resultado a través de un bot de Telegram.

3. Crear un Dockerfile
El Dockerfile configurará el entorno y ejecutará el script de Python.

4. Instrucciones para construir y ejecutar el contenedor Docker

1. Guardar los archivos:
   - Guarda el script de Python en un archivo llamado bot_temperatura.py.
   - Guarda el Dockerfile en el mismo directorio.

2. Construir la imagen Docker:
   - Abre una terminal en el directorio donde guardaste los archivos.
   - Ejecuta el siguiente comando para construir la imagen:
     docker build -t bot-temperatura .

3. Ejecutar el contenedor Docker:
   - Ejecuta el contenedor con el siguiente comando:
     docker run --name bot-temperatura -d --restart unless-stopped bot-temperatura

4. Interactuar con el bot de Telegram:
   - En Telegram, envía el comando /start y presionas el boton para recibir la temperatura actual de la CPU de tu Raspberry Pi.

