import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN

# Import handlers
from handlers.start import register_start_handler
from handlers.admin import register_admin_handlers
from handlers.ticket import register_ticket_handler
from handlers.bin_checker import register_bin_checker
from handlers.gpt import register_gpt_handler

# (Optional) Import keyboards if you want to send menus on /start, etc.
# from keyboards.main_menu import get_main_menu

# Set up logging
logging.basicConfig(level=logging.INFO, filename="logs/bot.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(name)s %(message)s")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def register_all_handlers(dp):
    register_start_handler(dp)
    register_admin_handlers(dp)
    register_ticket_handler(dp)
    register_bin_checker(dp)
    register_gpt_handler(dp)
    # Add more handler registrations as needed

async def on_startup(dispatcher):
    logging.info("Bot started.")
    # Optionally, initialize database or other resources here

def main():
    register_all_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

if __name__ == "__main__":
    main()

