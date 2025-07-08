from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton("💳 BIN Checker"),
        KeyboardButton("📝 Create Ticket"),
    )
    keyboard.add(
        KeyboardButton("🤖 GPT"),
        KeyboardButton("ℹ️ Help")
    )
    return keyboard