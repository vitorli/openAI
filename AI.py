﻿import openai
import telebot
# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = "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"
bot = telebot.TeleBot("5719702427:AAH82a3OnaEizRiphIG2w3HwjmXb-l16Kgg")

global model
global max_tokens
model = "text-davinci-003"
max_tokens = 1024


@bot.message_handler(commands=['curie'])
def start_message_1(message):
    global model
    model = "text-curie-001"
    bot.send_message(chat_id=message.from_user.id, text=f"Выбрана модель {model}")

@bot.message_handler(commands=['babbage'])
def start_message_2(message):
    global model
    model = "text-babbage-001"
    bot.send_message(chat_id=message.from_user.id, text=f"Выбрана модель {model}")

@bot.message_handler(commands=['ada'])
def start_message_3(message):
    global model
    model = "text-ada-001"
    bot.send_message(chat_id=message.from_user.id, text=f"Выбрана модель {model}")

@bot.message_handler(commands=['code_davinci'])
def start_message_4(message):
    global model
    model = "code-davinci-002"
    bot.send_message(chat_id=message.from_user.id, text=f"Выбрана модель {model}")

@bot.message_handler(commands=['code_cushman'])
def start_message_5(message):
    global model
    model = "code-cushman-001"
    bot.send_message(chat_id=message.from_user.id, text=f"Выбрана модель {model}")

@bot.message_handler(commands=['text_davinci'])
def start_message_6(message):
    global model
    model = "text-davinci-003"
    bot.send_message(chat_id=message.from_user.id, text=f"Выбрана модель {model}")

@bot.message_handler(commands=['max_tokens']) 
def max_tokens(message):
    bot.send_message(chat_id=message.from_user.id, text="Введите количество символов")
    bot.register_next_step_handler(message, max_tokens_next)


def max_tokens_next(message):
    global max_tokens
    max_tokens = message.text
    if int(max_tokens) > 3500 or int(max_tokens) < 5:
        bot.send_message(chat_id=message.from_user.id, text=f"Количество токенов должно быть в диапазоне от 5 до 3500")
        bot.register_next_step_handler(message, max_tokens_next)
    else:
        bot.send_message(chat_id=message.from_user.id, text=f"Количество символов изменено на {max_tokens}")



@bot.message_handler(func=lambda _: True)
def handle(message):
    global model
    completion = openai.Completion.create(
        engine=model,
        prompt=message.text,
        max_tokens=int(max_tokens),
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    bot.send_message(chat_id=message.from_user.id, text= completion.choices[0].text)

while True:
    try:
        bot.polling()
    except(BaseException):
        pass