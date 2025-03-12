import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7456446798:AAGw6DVZWwgVJT-u-6cDCrFfvaZ8HlGm5YE' 
bot = telebot.TeleBot(TOKEN)

STICKER_PATH = 'AnimatedSticker.tgs'
STICKER_PATH1 = 'AnimatedSticker1.tgs'

@bot.message_handler(commands=['start'])

def send_welcome(message):
    
    with open(STICKER_PATH, 'rb') as sticker:
            bot.send_document(message.chat.id, sticker)
    bot.reply_to(message, f"Сәлем, {message.from_user.first_name}! файлды алу үшін /getfile, командасын жазыңыз.")
    

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help information:</b>\n Файл алу үшін /getfile\n ', parse_mode='html' )

@bot.message_handler(commands=['showmembers'])
def showmemb(message):
    markup = InlineKeyboardMarkup()
    member1= InlineKeyboardButton('Tilek Aisha', callback_data='member1')
    member2= InlineKeyboardButton('Temirkhan_Yerazamat', callback_data='member2')
    markup.row(member1)
    markup.row(member2)
    bot.send_message(message.chat.id, "Студенттер: ", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: call.data in ['member1','member2'])
def send_members_inf(call):
    if call.data == 'member1':
        bot.send_message(call.message.chat.id, "member1 info")
    elif call.data == 'member2':
        bot.send_message(call.message.chat.id, "member2 info")
    return
    
@bot.message_handler(commands=['temirkhanyerazamat'])
def frog(message):
    bot.send_message(message.chat.id, 'GitHub: hqnters')

@bot.message_handler(commands=['tilekaisha'])
def git(message):
    bot.send_message(message.chat.id, 'ayshatilek')

@bot.message_handler(commands=['getfile'])
def send_file_buttons(message):
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("PowerPoint.pptx", callback_data='file1')
    btn2 = InlineKeyboardButton("Word.docx", callback_data='file2')
    btn_back = InlineKeyboardButton("Назад", callback_data='back')
    markup.add(btn1, btn2)
    markup.add(btn_back)
    with open(STICKER_PATH1, 'rb') as sticker:
            bot.send_document(message.chat.id, sticker)
    bot.send_message(message.chat.id, "Жаздырту керек файлды тандаңыз:", reply_markup=markup)
    bot.register_next_step_handler_by_chat_id(message.chat.id, lambda msg: delete_message(msg.chat.id, sent_message.message_id, sent_sticker))

@bot.callback_query_handler(func=lambda call: call.data in ['file1', 'file2', 'back'])
def send_selected_file(call):
    if call.data == 'back':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if os.path.exists(STICKER_PATH1):
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)  
        bot.send_message(call.message.chat.id, "Қайта бастағыңыз келе ме? /getfile командасын енгізіңіз")
        return
    
    file_paths = {
        'file1': 'example.txt',
        'file2': 'example.txt'
    }
    file_path = file_paths.get(call.data)
    if file_path and os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            bot.send_document(call.message.chat.id, file)

def delete_message(chat_id, message_id, sticker_message=None):
    bot.delete_message(chat_id, message_id)
    if sticker_message:
        bot.delete_message(chat_id, sticker_message.message_id)

@bot.message_handler()
def interact(message):
    text = message.text.lower()
    
    if text == 'қалайсың?':
        bot.reply_to(message, "Жақсы. Өзіңіз?")
    elif text == 'hello':
        bot.reply_to(message, f"Hello, {message.from_user.first_name}!")
    elif text == 'сәлем':
        bot.reply_to(message, f"Сәлем, {message.from_user.first_name}!")
    elif text == 'привет':
        bot.reply_to(message, f"Привет, {message.from_user.first_name}!")
    elif text == 'не істеп жатырсың?':
        bot.reply_to(message, "Сізбен сөйлесіп отырмын 😊")
    elif text == 'рахмет':
        bot.reply_to(message, "Оқасы жоқ! 😊")
    elif text == 'сен кімсің?':
        bot.reply_to(message, "Мен Telegram ботымын! 🤖")
    elif text == 'қош бол':
        bot.reply_to(message, "Қош бол! Кездескенше! 👋")
    elif text == 'қайдасың?':
        bot.reply_to(message, "Осындамын, сізбен бірге! 🌍")
    elif text == 'мені танисың ба?':
        bot.reply_to(message, f"Әрине, сен {message.from_user.first_name}! 😊")
    elif text == 'мен сені жақсы көремін':
        bot.reply_to(message, "Рақмет! Мен де сені жақсы көремін! ❤️")
    elif text == 'анекдот айтшы':
        bot.reply_to(message, "Қоян дүкенге кіріп: 'Сізде сәбіз бар ма?' – дейді. Дүкенші: 'Жоқ'. Ертеңінде тағы келеді: 'Сәбіз бар ма?'. Дүкенші: 'Жоқ'. Үшінші күні дүкенші сәбіз әкеліп қояды. Қоян тағы келеді: 'Сізде сәбіз бар ма?' – 'Иә, бар'. – 'Фуу, маған болмайды екен...' 🐰😂")
    elif text == 'ауа райы қандай?':
        bot.reply_to(message, "Оны интернеттен қарап көруге кеңес беремін! ☀️🌧️")
    elif text == 'ботсың ба?':
        bot.reply_to(message, "Иә, мен ботпын, бірақ достыққа дайынмын! 🤖")
    else:
        bot.reply_to(message, "Кешіріңіз, бұл сұраққа жауап беруге дайын емеспін. 😊")

if __name__ == '__main__':
    print("Bot activated...")
    bot.infinity_polling()
    