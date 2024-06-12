import os
import time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Token del bot de Telegram (sustituir por tu propio token)
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT'
CHAT_ID = 'YOUR_CHAT_EDIT'  # ID del chat o del grupo donde enviar los mensajes

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def get_cpu_temperature():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temp_str = file.read().strip()
            temperature = int(temp_str) / 1000.0
            return temperature
    except FileNotFoundError:
        return "No se pudo encontrar el archivo de temperatura."
    except Exception as e:
        return f"Error al leer la temperatura: {e}"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Obtener temperatura", callback_data="get_temp"))
    bot.send_message(message.chat.id, "Bienvenido! Presiona el botón para obtener la temperatura de la CPU.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "get_temp")
def callback_query(call):
    temperature = get_cpu_temperature()
    if isinstance(temperature, float):
         bot.send_message(call.message.chat.id, f"La temperatura actual de la CPU es: {temperature:.2f} °C")
    else:
         bot.send_message(call.message.chat.id, temperature)

if __name__ == "__main__":
     bot.polling()
