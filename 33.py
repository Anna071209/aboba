import os
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import sqlite3
import requests
from main import BOT_TOKEN
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile, URLInputFile
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


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
async def next1(message: types.Message):
    scence = 1
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/школа')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await message.reply(q[0], reply_markup=kb)
    await asyncio.sleep(1)
    await bot.send_audio(message.chat.id, au)

@dp.message(Command('школа'))
async def next2(message: types.Message):
    scence = 2
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/кабинет_физики')], [KeyboardButton(text='/кабинет_биологии')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await message.reply(q[0], reply_markup=kb)
    await asyncio.sleep(1)
    await bot.send_audio(message.chat.id, au)

@dp.message(Command('кабинет_физики'))
async def next3(message: types.Message):
    scence = 3
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/кабинет_биологии')], [KeyboardButton(text='/в_кабинет_физики')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await message.reply(q[0], reply_markup=kb)
    await asyncio.sleep(1)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('кабинет_биологии'))
async def next4(message: types.Message):
    scence = 4
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/на_урок_русского')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await message.reply(q[0], reply_markup=kb)
    await asyncio.sleep(1)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('в_кабинет_физики'))
async def next5(message: types.Message):
    scence = 5
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    reply_keyboard = [[KeyboardButton(text="/start")]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('на_урок_русского'))
async def next6(message: types.Message):
    scence = 6
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/в_коридор')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await message.reply(q[0], reply_markup=kb)
    await asyncio.sleep(1)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('в_коридор'))
async def next7(message: types.Message):
    scence = 7
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/в_столовую')], [KeyboardButton(text='/в_библиотеку')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await message.reply(q[0], reply_markup=kb)
    await asyncio.sleep(1)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('в_столовую'))
async def next8(message: types.Message):
    scence = 8
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/Добрый_кола')], [KeyboardButton(text='/Булочка')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await message.reply(q[0], reply_markup=kb)
    await asyncio.sleep(1)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('в_библиотеку'))
async def next9(message: types.Message):
    scence = 9
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/взять_книгу')], [KeyboardButton(text='/сделать_уроки_по_математике')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('взять_книгу'))
async def next10(message: types.Message):
    scence = 10
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/в_кабинет_математики')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('сделать_уроки_по_математике'))
async def next11(message: types.Message):
    scence = 11
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/в_кабинет_математики')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('в_кабинет_математики'))
async def next12(message: types.Message):
    scence = 12
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/коридорик')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('Добрый_кола'))
async def next13(message: types.Message):
    scence = 13
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/кабинет_математики')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('Булочка'))
async def next14(message: types.Message):
    scence = 14
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/в_кабинет_математики')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('кабинет_математики'))
async def next15(message: types.Message):
    scence = 15
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    get = requests.get(t[0])
    reply_keyboard = [[KeyboardButton(text='/в_коридорик')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('в_коридорик'))
async def next16(message: types.Message):
    scence = 16
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/Прогулять_всё_к_чёрту')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    await message.reply(q[0], reply_markup=kb)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('Прогулять_всё_к_чёрту'))
async def next58(message: types.Message):
    scence = 58
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)



@dp.message(Command('коридорик'))
async def next17(message: types.Message):
    scence = 17
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/с_другом')], [KeyboardButton(text='/на_урок_корейского')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    await message.reply(q[0], reply_markup=kb)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('с_другом'))
async def next18(message: types.Message):
    scence = 18
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/зайти')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('зайти'))
async def next46(message: types.Message):
    scence = 46
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/прогулять')], [KeyboardButton(text='/на_урок')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    await message.reply(q[0], reply_markup=kb)
    await bot.send_audio(message.chat.id, au)


@dp.message(Command('на_урок_корейского'))
async def next19(message: types.Message):
    scence = 19
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/у_учительницы_по_истории')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    get = requests.get(t[0])
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('у_учительницы_по_истории'))
async def next41(message: types.Message):
    scence = 41
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    l = cur.execute(f"SELECT dialog FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/на_урок')], [KeyboardButton(text='/прогулять')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    au = FSInputFile(f'data/{l[0]}.mp3')
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('на_урок'))
async def next25(message: types.Message):
    scence = 25
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('прогулять'))
async def next26(message: types.Message):
    scence = 26
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/поднять')], [KeyboardButton(text='/не_поднимать')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('не_поднимать'))
async def next27(message: types.Message):
    scence = 27
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('поднять'))
async def next28(message: types.Message):
    scence = 28
    t = cur.execute(f"SELECT image FROM scenes WHERE id = '{scence}'").fetchone()
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/1')], [KeyboardButton(text='/2')], [KeyboardButton(text='/3')],
                      [KeyboardButton(text='/4')], [KeyboardButton(text='/5')], [KeyboardButton(text='/6')],
                      [KeyboardButton(text='/7')], [KeyboardButton(text='/8')], [KeyboardButton(text='/9')],
                      [KeyboardButton(text='/10')], [KeyboardButton(text='/11')], [KeyboardButton(text='/12')], ]
    get = requests.get(t[0])
    image = URLInputFile(get.url, filename="python-logo.png")
    await bot.send_photo(message.chat.id, image)
    await asyncio.sleep(1)
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('1'))
async def next29(message: types.Message):
    scence = 29
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('2'))
async def next30(message: types.Message):
    scence = 30
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('3'))
async def next31(message: types.Message):
    scence = 31
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('4'))
async def next32(message: types.Message):
    scence = 32
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('5'))
async def next33(message: types.Message):
    scence = 33
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('6'))
async def next34(message: types.Message):
    scence = 34
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('7'))
async def next35(message: types.Message):
    scence = 35
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('8'))
async def next36(message: types.Message):
    scence = 36
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('9'))
async def next37(message: types.Message):
    scence = 37
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('10'))
async def next38(message: types.Message):
    scence = 38
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('11'))
async def next39(message: types.Message):
    scence = 39
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


@dp.message(Command('12'))
async def next40(message: types.Message):
    scence = 40
    q = cur.execute(f"SELECT text FROM scenes WHERE id = '{scence}'").fetchone()
    reply_keyboard = [[KeyboardButton(text='/start')]]
    kb = ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
    await message.reply(q[0], reply_markup=kb)


if __name__ == '__main__':
    asyncio.run(main())