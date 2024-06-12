# Usamos la imagen oficial de Python como base
FROM python:3.9-slim

# Instalamos las dependencias necesarias
RUN pip install pyTelegramBotAPI

# Añadimos nuestro script de Python al contenedor
ADD bot_temperatura.py /bot_temperatura.py

# Configuramos el comando de inicio
CMD ["python", "/bot_temperatura.py"]
