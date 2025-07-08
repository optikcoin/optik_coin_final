from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_confirmation_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(
        KeyboardButton("✅ Confirm"),
        KeyboardButton("❌ Cancel")
    )
    return keyboard