import os

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import sqlite3
import requests

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile, URLInputFile
from aiogram.utils.chat_action import ChatActionSender
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = '7068372821:AAEVoaAjnbyrzKcmznq4KlvuLH5RNCS95wA'
con = sqlite3.connect("scene1.sqlite")
cur = con.cursor()
dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)


async def main():
    await dp.start_polling(bot)


@dp.message(Command('start'))
async def entrance(message: types.Message):
    text = (' Если Вы захотите закончить игру напишите слово "stop"\n ☆*:.｡..｡.:*☆---☆*:.｡..｡.:*☆ \n'
            'Вы проснулись в своей комнате.')
    reply_keyboard = [[KeyboardButton(text="/stop")], [KeyboardButton(text="/спальня")]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(text, reply_markup=kb)


@dp.message(Command('stop'))
async def exit_handler(message: types.Message):
    text = 'Вы достали свой перочиный нож из внутреннего кармана и перерезали себе горло'
    reply_keyboard = [[KeyboardButton(text="/start")]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(text, reply_markup=kb)


@dp.message(Command('спальня'))
async def next_room(message: types.Message):
    scence = 1
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/школа')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)

@dp.message(Command('школа'))
async def next_room(message: types.Message):
    scence = 2
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/кабинет физики')], [KeyboardButton(text='/кабинет биологии')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)

@dp.message(Command('кабинет физики'))
async def next_room(message: types.Message):
    scence = 3
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/кабинет биологии')], [KeyboardButton(text='/в кабинет физики')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)


@dp.message(Command('кабинет биологии'))
async def next_room(message: types.Message):
    scence = 4
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='')], [KeyboardButton(text='')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)


@dp.message(Command('в кабинет физики'))
async def next_room(message: types.Message):
    scence = 5
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='')], [KeyboardButton(text='')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)


@dp.message(Command('на урок русского'))
async def next_room(message: types.Message):
    scence = 6
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='')], [KeyboardButton(text='')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)

@dp.message(Command('в коридор'))
async def next_room(message: types.Message):
    scence = 7
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='')], [KeyboardButton(text='')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)


@dp.message(Command('в столовую'))
async def next_room(message: types.Message):
    scence = 8
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='')], [KeyboardButton(text='')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)


@dp.message(Command('в библиотеку'))
async def next_room(message: types.Message):
    scence = 9
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='')], [KeyboardButton(text='')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)


@dp.message(Command('взять книгу'))
async def next_room(message: types.Message):
    scence = 10
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='')], [KeyboardButton(text='')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)

@dp.message(Command('сделать уроки по математике'))
async def next_room(message: types.Message):
    scence = 11
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='')], [KeyboardButton(text='')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)


@dp.message(Command('в кабинет математики'))
async def next_room(message: types.Message):
    scence = 12
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='')], [KeyboardButton(text='')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)


@dp.message(Command('Добрый кола'))
async def next_room(message: types.Message):
    scence = 13
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='')], [KeyboardButton(text='')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)


@dp.message(Command('Булочка'))
async def next_room(message: types.Message):
    scence = 14
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='')], [KeyboardButton(text='')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)


@dp.message(Command('кабинет математики'))
async def next_room(message: types.Message):
    scence = 15
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='')], [KeyboardButton(text='')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    # au = FSInputFile(f'{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    # await bot.send_audio(message.chat.id, au)


if __name__ == '__main__':
    asyncio.run(main())