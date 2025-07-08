from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

async def start_command(message: types.Message):
    await message.reply(
        "👋 Welcome to Optik Coin Carding Bot!\n"
        "Use /help to see available commands."
    )

def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_command, Command("start"))