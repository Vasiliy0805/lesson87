from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo

bot = Bot("7287345480:AAHJhiqftTfUlaUY7wKCMUtNfEUUk0jfyfE")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Открыть веб  страницу", web_app= WebAppInfo(url = "https://")))
    await message.answer("привет, ты кто?", reply_markup = markup)

executor.start_polling(dp)
