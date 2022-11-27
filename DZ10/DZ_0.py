from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='токен')
dp = Dispatcher(bot)

text = ''

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    mess = f'привет'
    await message.reply(mess)


@dp.message_handler(commands=['website'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup() #  цепляется непосредственно к сообщениям
    il = types.InlineKeyboardButton(text='line_button', url='https://mail.ru/')
    markup.add(il)
    await bot.send_message(message.chat.id, 'InlineKeyboard', reply_markup=markup)


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, input_field_placeholder="Ваше сообщение")
    b1 = types.KeyboardButton('/Добавить')  # цепляется к низу экрана  устройства
    markup.add(b1)
    b2 = types.KeyboardButton('/Посмотреть')  # цепляется к низу экрана  устройства
    markup.add(b2)
    await bot.send_message(message.chat.id, 'Сопроводительное сообщение', reply_markup=markup)


# @dp.message_handler(commands=['Посмотреть'])
# async def help(message: types.Message):
#     # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, input_field_placeholder="Ваше сообщение")
#     with open('data_tel.txt', 'r', encoding='utf-8') as file:
#         data = ''.join(file.readlines())
#     # b2 = types.KeyboardButton('Кнопка 2', )  # цепляется к низу экрана вашего устройства
#     # markup.add(b2)
#     await bot.send_message(message.chat.id, 'смотри')


# @dp.message_handler(commands=['Добавить'])
# async def help(message: types.Message):
#     # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, input_field_placeholder="Ваше сообщение")
#     with open('data_tel.txt', 'a', encoding='utf-8') as file:
#         file.write(f'{message.text}\n')
#
#     with open('data_tel.txt', 'r', encoding='utf-8') as file:
#         data = ''.join(file.readlines())
#     # b2 = types.KeyboardButton('Кнопка 2', )  # цепляется к низу экрана  устройства
#     # markup.add(b2)
#     await message.reply(f'{data}')


@dp.message_handler(content_types=['text'])
async def calc(message: types.Message):
    if message.text.endswith('добавить'):
        with open('data_tel.txt', 'a', encoding='utf-8') as file:
            file.write(f'{message.text[0:-8]}\n')
            await bot.send_message(message.chat.id, 'Добавил')

    elif message.text.endswith('посмотреть'):
        with open('data_tel.txt', 'r', encoding='utf-8') as file:
            data = ''.join(file.readlines())
        await bot.send_message(message.chat.id, data)

    elif message.text.endswith('найти'):
        with open('data_tel.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
            for i in data:
                if message.text[0:-5] in i:
                    await bot.send_message(message.chat.id, i)
                else:
                    continue

    else:
        await message.reply(f'Нет команды в конце строки')
    # b2 = types.KeyboardButton('Кнопка 2', )  # цепляется к низу экрана вашего устройства
    # markup.add(b2)


executor.start_polling(dp)
