from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import asyncio

API_URL = 'http://127.0.0.1:8000/api/trainings/'

bot = Bot(token='7203373895:AAHCQRh4DmiCxOCdOOs-GxKbb6ZWGt9AOuI')
dp = Dispatcher()


@dp.message(command=['start'])
async def start(message: types.Message):
    response = requests.get(API_URL)
    data = response.json()

    keyboard = InlineKeyboardMarkup(row_width=1)
    for item in data:
        button = InlineKeyboardButton(text=item['weight_category'], callback_data=f"training_{item['id']}")
        keyboard.add(button)

    await message.answer("esingizni yozin:", reply_markup=keyboard)


@dp.callback_query(lambda c: c.data.startswith('training_'))
async def process_callback(callback_query: types.CallbackQuery):
    training_id = callback_query.data.split('_')[1]
    response = requests.get(f"{API_URL}{training_id}/")
    training = response.json()

    message_text = (
        f"bu ves uchun trenirovka: {training['weight_category']}\n"
        f"pisaniya: {training['description']}\n"
        f"vaqti: {training['duration']} минут\n"
        f"qiyinligi: {training['intensity']}"
    )

    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, message_text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
