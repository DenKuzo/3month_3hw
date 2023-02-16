import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

# Bot это токен бота
load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
db = Dispatcher(bot)


@db.message_handler(commands=['start', 'hello'])
async def start_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f'привет {massage.from_user.first_name}')
    await massage.answer('это ансфер')
    await massage.reply(massage.from_user.first_name)


@db.message_handler(commands=['quiz'])
async def quiz1(massage: types.Message):
    # создание кнопок
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)
    # привязать кнопки к опроснику
    # создание опросника

    ques = 'кто ты воин?'
    answer = [
        'Бетмен-рыцарь ночи',
        'томас шелби из семьи острые козырьки',
        'спанч боб:квадратные штаны',
        'Ахилес! Сын пелея ',
        'диктор канала "Мастерская настроения"',
        'оптимус прайм последний прайм'
    ]
    # await massage.answer_poll()
    await bot.send_poll(
        chat_id=massage.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='ты ахилесс',
        open_period=15,
        reply_markup=markup
    )


@db.callback_query_handler(text='button')
# перехватчик нажатия кнопки
async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='beka')
    markup.add(button)
    ques = 'кто это?'
    answer = [
        'Бетмен-рыцарь ночи',
        'спанч боб:квадратные штаны',
        'Ахилес! Сын пелея ',
        'оптимус прайм последний прайм'
    ]
    photo = open('images/nBkSUh.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='это бетмен ты угадал',
        open_period=30,
        reply_markup=markup
    )


@db.callback_query_handler(text='beka')
async def quiz3(call: types.CallbackQuery):
    answer = [
        'Scatman',
        'Анигиляторная пушка',
        'Рикардо Милос',
        'По какому каналу будете показывать?',

    ]
    ques = 'угадай мем на картинке'
    photo = open('images/images.jpeg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='это coffing dance ты угадал!',
        open_period=30)


@db.message_handler()
async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)
    await massage.answer('что-то еще?')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
