'''
2.1. Створити команду "Start", яка буде вітатись з користувачем.
     При чому, бот повинен назвати користувача за іменем, яке він зазначив при реєстрації у Телеграмі.

2.2. Додайте боту команду "Додаткове меню" (опис - довільний).
     При натисканні на цей пункт меню користувач повинен отримати наступне вбудоване (inline).
       - перехід до клавіатури;
       - введення прізвища;
       - введення віку.

    2.2.1. На клавіатурі повинно бути 2 кнопки:
         - отримувати новини
         - видалити чат

        2.2.1.1. Кожні 1 хвилини користувачу надсилається довільне повідомлення (всього - 10)

        2.2.2.2. Видаляється історія чату
                 (всі меседжі мають id, починаючи з 0, в залежності від того, коли вони публікувались)

    2.2.2. Якщо користувач вводить прізвище - його потрібно записати у файл.

    2.2.3. Якщо користувач вводить вік - потрібно просто відповісти "Дякую".

3. Виконати запуск ботів з віддаленого сервера.
'''
# import csv
# import random
# import time
#
# # 5811216138:AAE0AOTovj5JjD_vijg8UFxNHlO2T9V6eP0
#
# import telebot
# from random import randint
# from telebot import types
#
# dice = 0
# part = ""
# bot = telebot.TeleBot("5811216138:AAE0AOTovj5JjD_vijg8UFxNHlO2T9V6eP0")
#
# def choose_roll_number(user_id=None):
#     global part
#     part = "roll"
#     roll_keyboard = types.ReplyKeyboardMarkup(True, True)
#     roll_keyboard.row("1", "2", "3", "4", "5")
#     roll_keyboard.row("6", "7", "8", "9", "10")
#     if user_id:
#         bot.send_message(user_id, "Choose number of rolls", reply_markup=roll_keyboard)
#     else:
#         bot.send_message("Choose number of rolls", reply_markup=roll_keyboard)
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, f"Hello, {message.chat.first_name}! Choose the command.")
#     print(f"Greeted with {message.chat.username}")
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     global dice
#     if call.data == "dice6":
#         dice = 6
#     elif call.data == "dice12":
#         dice = 12
#     elif call.data == "dice20":
#         dice = 20
#     print(call)
#     bot.send_message(call.from_user.id, f"Your dice roll: {dice}")
#     choose_roll_number(call.from_user.id)
#
# @bot.message_handler(commands=['roll_dice'])
# def roll_the_dice(message):
#     global part
#     part = "begin"
#     dice_menu = types.InlineKeyboardMarkup()
#     dice6 = types.InlineKeyboardButton(text="D6", callback_data="dice6")
#     dice12 = types.InlineKeyboardButton(text="D12", callback_data="dice12")
#     dice20 = types.InlineKeyboardButton(text="D20", callback_data="dice20")
#     dice_menu.add(dice6, dice12, dice20)
#     bot.send_message(message.chat.id, "Choose dice or enter by yourself: ", reply_markup=dice_menu)
#
# @bot.message_handler(commands=['additional_menu'])
# def additional_menu(message):
#     additional_menu_buttons = types.InlineKeyboardMarkup()
#     keyboard_btn = types.InlineKeyboardButton(text="До клавіатури", callback_data="keyboard")
#     surname_btn = types.InlineKeyboardButton(text="Введення прізвища", callback_data="surname")
#     age_btn = types.InlineKeyboardButton(text="Введення віку", callback_data="age")
#     additional_menu_buttons.add(keyboard_btn, surname_btn, age_btn)
#     bot.send_message(message.chat.id, "Additional Menu:", reply_markup=additional_menu_buttons)
#
#
#
# # ________________________________________________________________________________________
#
# @bot.message_handler(content_types=['text'])
# def get_text(message):
#     if part == "begin":
#         global dice
#         try:
#             dice = int(message.text)
#             bot.send_message(message.chat.id, f"Your dice roll: {dice}")
#             choose_roll_number(message.chat.id)
#         except Exception:
#             bot.send_message(message.chat.id, "Wrong number. Please try again: ")
#     elif part == "roll":
#         rolls = int(message.text)
#         result = ""
#         for i in range(rolls):
#             result += "\n"+str(random.randint(1, dice))
#         bot.send_message(message.chat.id, f"Dice: {dice}, Rolls: {rolls}. Let's roll:\n{result}")
#
#
# bot.polling()


import time
from pkgutil import get_data


def get_id():
    return {1, 2, 3}


def add_data():
    return {1, 2, 3}


def add_msg_id():
    return {1, 2, 3}


import random
import telebot
from telebot import types
from bebebe import save_user_data

dice = 0
part = ""
bot = telebot.TeleBot("5811216138:AAE0AOTovj5JjD_vijg8UFxNHlO2T9V6eP0")


def choose_roll_number(user_id=None):
    global part
    part = "roll"
    roll_keyboard = types.ReplyKeyboardMarkup(True, True)
    roll_keyboard.row("1", "2", "3", "4", "5")
    roll_keyboard.row("6", "7", "8", "9", "10")
    if user_id:
        bot.send_message(user_id, "Choose the number of rolls", reply_markup=roll_keyboard)
    else:
        bot.send_message("Choose the number of rolls", reply_markup=roll_keyboard)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Hello, {message.chat.first_name}! Choose a command.")
    print(message.chat)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global dice
    if call.data == "dice6":
        dice = 6
    elif call.data == "dice12":
        dice = 12
    elif call.data == "dice20":
        dice = 20
    elif call.data == "keyboard":
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row("Receive news", "Delete chat")
        bot.send_message(call.from_user.id, "Choose something", reply_markup=keyboard)
        return
    # elif call.data == "surname":
    #     part = "surname"
    #     bot.send_message(call.from_user.id, "Enter your surname")
    #     save_user_data(call.from_user.id, call.from_user.first_name, call.from_user.message, 0)
    #
    # elif call.data == "age":
    #     part = "age"
    #     bot.send_message(call.from_user.id, "Enter your age")
    #     save_user_data(call.from_user.id, call.from_user.first_name, "", part)

    bot.send_message(call.from_user.id, f"Your dice roll: {dice}")
    choose_roll_number(call.from_user.id)


@bot.message_handler(commands=['roll_dice'])
def roll_the_dice(message):
    global part
    part = "begin"
    dice_menu = types.InlineKeyboardMarkup()
    dice6 = types.InlineKeyboardButton(text="D6", callback_data="dice6")
    dice12 = types.InlineKeyboardButton(text="D12", callback_data="dice12")
    dice20 = types.InlineKeyboardButton(text="D20", callback_data="dice20")
    dice_menu.add(dice6, dice12, dice20)
    bot.send_message(message.chat.id, "Choose a dice or enter the number yourself: ", reply_markup=dice_menu)


@bot.message_handler(commands=['additional_menu'])
def additional_menu(message):
    additional_menu_buttons = types.InlineKeyboardMarkup()
    b_keyboard = types.InlineKeyboardButton(text="Go to keyboard", callback_data="keyboard")
    b_surname = types.InlineKeyboardButton(text="Add surname", callback_data="surname")
    b_age = types.InlineKeyboardButton(text="Add age", callback_data="age")
    additional_menu_buttons.add(b_keyboard, b_surname, b_age)
    bot.send_message(message.chat.id, "Additional Menu:", reply_markup=additional_menu_buttons)


def send_news(message):
    for i in range(10):
        news_message = f"This is news {i} of 10"
        bot.send_message(message.chat.id, news_message)
        time.sleep(5)


@bot.callback_query_handler(func=lambda call: call.data == "keyboard")
def keyboard_callback(call):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    news_btn = types.KeyboardButton("Отримувати новини")
    delete_btn = types.KeyboardButton("Видалити чат")
    keyboard.add(news_btn, delete_btn)
    bot.send_message(call.from_user.id, "Keyboard menu:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Отримувати новини")
def receive_news(message):
    send_news(message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data == "surname")
def enter_surname(call):
    bot.send_message(call.from_user.id, "Please enter your surname:")
    bot.register_next_step_handler(call.message, save_surname)


def save_surname(message, call):
    global part
    part = "surname"
    user_id = message.from_user.id
    # user_name = message.from_user
    # surname = message.text
    # with open('user_data.csv', mode='a', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow([user_id, user_name, surname])
    save_user_data(call.from_user.id, call.from_user.first_name, message.text, 0)
    bot.send_message(user_id, "Your surname has been saved.")


@bot.message_handler(content_types=['text'])
def get_text(message):
    global part

    print('Here', message)

    if part == "begin":
        global dice
        try:
            dice = int(message.text)
            bot.send_message(message.chat.id, f"Your dice roll: {dice}")
            choose_roll_number(message.chat.id)
        except Exception:
            bot.send_message(message.chat.id, "Wrong number. Please try again: ")

    elif part == "roll":
        rolls = int(message.text)
        result = ""
        for i in range(rolls):
            result += "\n" + str(random.randint(1, dice))
        bot.send_message(message.chat.id, f"Dice: {dice}, Rolls: {rolls}. Let's roll:\n{result}")

    elif part == "surname":
        bot.send_message(message.from_user.id, "Enter your surname")
        save_user_data(message.from_user.id, message.from_user.first_name, message.text, 0)
        enter_surname()

    elif message.text == "Receive news":
        send_news(message)


    elif message.text == "Delete chat":
        for i in get_id():
            try:
                bot.delete_message(message.chat.id, i[0])
            except Exception:
                print("Chat can`t be cleared")
                pass


bot.polling()

