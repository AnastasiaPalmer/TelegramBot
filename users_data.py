import time
import random
import telebot
from telebot import types
from bebebe import save_user_data

dice = 0
part = ""
bot = telebot.TeleBot("5811216138:AAE0AOTovj5JjD_vijg8UFxNHlO2T9V6eP0")

@bot.message_handler(commands=['additional_menu'])
def additional_menu(message):
    additional_menu_buttons = types.InlineKeyboardMarkup()
    b_keyboard = types.InlineKeyboardButton(text="Go to keyboard", callback_data="keyboard")
    b_surname = types.InlineKeyboardButton(text="Add surname", callback_data="Add surname")
    b_age = types.InlineKeyboardButton(text="Add age", callback_data="Add age")
    additional_menu_buttons.add(b_keyboard, b_surname, b_age)
    bot.send_message(message.chat.id, "Additional Menu:", reply_markup=additional_menu_buttons)

def choose_roll_number(user_id):
    global part
    part = "roll"
    roll_keyboard = types.ReplyKeyboardMarkup(True, True)
    roll_keyboard.row("1", "2", "3", "4", "5")
    roll_keyboard.row("6", "7", "8", "9", "10")
    bot.send_message(user_id, "Choose the number of rolls", reply_markup=roll_keyboard)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Hello, {message.chat.first_name}! Choose a command.")
    print(message.chat)

@bot.message_handler(commands=['roll_dice'])
def roll_the_dice(message):
    global part
    part = "roll"
    dice_menu = types.InlineKeyboardMarkup()
    dice6 = types.InlineKeyboardButton(text="D6", callback_data="dice6")
    dice12 = types.InlineKeyboardButton(text="D12", callback_data="dice12")
    dice20 = types.InlineKeyboardButton(text="D20", callback_data="dice20")
    dice_menu.add(dice6, dice12, dice20)
    bot.send_message(message.chat.id, "Choose a dice to roll: ", reply_markup=dice_menu)

def send_news(message):
    for i in range(1, 11):
        news_message = f"This is news {i} of 10"
        bot.send_message(message.chat.id, news_message)
        time.sleep(2)

# @bot.callback_query_handler(func=lambda call: call.data == "keyboard")
# def keyboard_callback(call):
#     keyboard = types.ReplyKeyboardMarkup(row_width=2)
#     news_btn = types.KeyboardButton("Отримувати новини")
#     delete_btn = types.KeyboardButton("Видалити чат")
#     keyboard.add(news_btn, delete_btn)
#     bot.send_message(call.from_user.id, "Keyboard menu:", reply_markup=keyboard)

# @bot.message_handler(func=lambda message: message.text == "Отримувати новини")
# def receive_news(message):
#     send_news(message.chat.id)


# @bot.callback_query_handler(func=lambda call: call.data == "surname")
# def enter_surname(call):
#     bot.send_message(call.from_user.id, "Please enter your surname:")
#     bot.register_next_step_handler(call.message, save_surname)

# def save_surname(message):
#     global part
#     part = "surname"
#     user_id = message.from_user.id
#     # user_name = message.from_user
#     # surname = message.text
#     # with open('user_data.csv', mode='a', newline='') as file:
#     #     writer = csv.writer(file)
#     #     writer.writerow([user_id, user_name, surname])
#     save_user_data(message.from_user.id, message.from_user.first_name, message.text, 0)
#     bot.send_message(user_id, "Your surname has been saved.")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global part, dice
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
    elif call.data == "Add surname":
        part = "surname"
        bot.send_message(call.from_user.id, "Enter your surname")

    elif call.data == "Add age":
        part = "age"
        bot.send_message(call.from_user.id, "Enter your age")



    bot.send_message(call.from_user.id, f"Your dice roll: {dice}")
    choose_roll_number(call.from_user.id)

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
            result += "\n"+str(random.randint(1, dice))
        bot.send_message(message.chat.id, f"Dice: {dice}, Rolls: {rolls}. Let's roll:\n{result}")

    elif part == "surname":
        try:
            save_user_data(message.from_user.id, message.from_user.first_name, message.text)
            bot.send_message(message.chat.id, "Surname saved.")
        except Exception:
            print("Error in part surname")
            pass

    elif part == "age":
        try:
            save_user_data(message.from_user.id, message.from_user.first_name, str(message.from_user.last_name), message.text)
            bot.send_message(message.chat.id, "Age saved.")
        except Exception:
            print("Error in part age")
            pass

    elif message.text == "Receive news":
        send_news(message)

    # elif message.text == "Delete chat":
    #     bot.delete_message(message.chat.id, message.message_id)
    # else:
    #     bot.send_message(message.chat.id, "Invalid command.")

bot.polling()
