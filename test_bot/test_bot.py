from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
import asyncio

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот в онлайне')


async def calculate_factorial(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Введите неотрицательное число, для которого вы хотите посчитать факториал.")


@dp.message_handler(lambda message: message.text.isdigit())
async def calculate(message: types.Message):
    num = int(message.text)
    await message.reply(f"Вычисляю факториал числа {num}...")

    # Разбиваем вычисление факториала на два потока
    half = num // 2
    tasks = [calculate_factorial(1, half), calculate_factorial(half + 1, num)]
    results = await asyncio.gather(*tasks)

    total_result = results[0] * results[1]
    await message.reply(f"Факториал числа {num} равен {total_result}")


@dp.message_handler(lambda message: not message.text.isdigit())
async def not_a_number(message: types.Message):
    await message.reply("Пожалуйста, введите целое неотрицательное число.")

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)