from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_bin_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton("🔍 Check BIN"),
        KeyboardButton("📋 My BINs"),
    )
    keyboard.add(
        KeyboardButton("🔙 Back")
    )
    return keyboard