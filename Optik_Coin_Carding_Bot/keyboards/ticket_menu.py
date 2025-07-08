from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_ticket_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton("📝 Create Ticket"),
        KeyboardButton("📋 My Tickets"),
    )
    keyboard.add(
        KeyboardButton("🔙 Back")
    )
    return keyboard