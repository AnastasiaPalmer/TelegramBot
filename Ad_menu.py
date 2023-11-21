import time
import random
import telebot
from telebot import types
from bebebe import save_user_data

bot = telebot.TeleBot("5811216138:AAE0AOTovj5JjD_vijg8UFxNHlO2T9V6eP0")

@bot.message_handler(commands=['start'])
def start(message):
    # Отримання імені користувача з даних профілю
    user_name = message.chat.first_name
    bot.send_message(message.chat.id, f"Hello, {user_name}! Choose a command.")


@bot.message_handler(commands=['additional_menu'])
def additional_menu(message):
    additional_menu_buttons = types.InlineKeyboardMarkup()
    b_keyboard = types.InlineKeyboardButton(text="Go to keyboard", callback_data="keyboard")
    b_surname = types.InlineKeyboardButton(text="Add surname", callback_data="surname")
    b_age = types.InlineKeyboardButton(text="Add age", callback_data="age")
    additional_menu_buttons.add(b_keyboard, b_surname, b_age)
    bot.send_message(message.chat.id, "Additional Menu:", reply_markup=additional_menu_buttons)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Hello, {message.chat.first_name}! Choose a command.")
    print(message.chat)

def send_news(chat_id):
    for i in range(1, 11):
        news_message = f"This is news {i} of 10"
        bot.send_message(chat_id, news_message)
        #time.sleep(60)  # Очікування 1 хвилину
        time.sleep(2)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "keyboard":
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        news_btn = types.KeyboardButton("Receive news")
        delete_btn = types.KeyboardButton("Delete chat")
        keyboard.add(news_btn, delete_btn)
        bot.send_message(call.from_user.id, "Choose something", reply_markup=keyboard)
    elif call.data == "surname":
        bot.send_message(call.from_user.id, "Enter your surname")
        bot.register_next_step_handler(call.message, save_surname)
    elif call.data == "age":
        bot.send_message(call.from_user.id, "Enter your age")
        bot.register_next_step_handler(call.message, save_age)


def save_surname(message):
    user_id = message.from_user.id
    save_user_data(message.from_user.id, message.from_user.first_name, message.text)
    bot.send_message(user_id, "Your surname has been saved.")


def save_age(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Age saved. Thank you!")


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == "Receive news":
        send_news(message.chat.id)
    elif message.text == "Delete chat":
        bot.delete_message(message.chat.id, message.message_id)
    else:
        bot.send_message(message.chat.id, "Invalid command.")


bot.polling()
