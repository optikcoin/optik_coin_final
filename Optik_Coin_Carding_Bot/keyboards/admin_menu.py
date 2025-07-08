from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_admin_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton("👤 Users"),
        KeyboardButton("➕ Add User"),
        KeyboardButton("➖ Remove User"),
    )
    keyboard.add(
        KeyboardButton("📊 Stats"),
        KeyboardButton("🔙 Back")
    )
    return keyboard