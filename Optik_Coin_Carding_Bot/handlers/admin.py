from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

ADMIN_IDS = [123456789]  # Replace with real admin Telegram user IDs

async def admin_start(message: Message):
    if message.from_user.id in ADMIN_IDS:
        await message.reply("Welcome, admin! Use /users to see all users.")
    else:
        await message.reply("You are not authorized to use admin commands.")

async def list_users(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.reply("You are not authorized.")
        return
    # Example: Fetch users from database
    from database import get_all_users
    users = get_all_users()
    if users:
        user_list = "\n".join([f"{u[1]} (Balance: {u[2]})" for u in users])
        await message.reply(f"Users:\n{user_list}")
    else:
        await message.reply("No users found.")

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_start, Command("admin"))
    dp.register_message_handler(list_users, Command("users"))