from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

TICKET_ADMIN_ID = 123456789  # Replace with your admin Telegram user ID

async def create_ticket(message: types.Message):
    issue = message.get_args()
    if not issue:
        await message.reply("Please describe your issue. Example: /ticket I have a problem with my balance.")
        return

    # Forward the ticket to the admin
    await message.bot.send_message(
        TICKET_ADMIN_ID,
        f"📩 New ticket from @{message.from_user.username or message.from_user.id}:\n{issue}"
    )
    await message.reply("Your ticket has been submitted. An admin will contact you soon.")

def register_ticket_handler(dp: Dispatcher):
    dp.register_message_handler(create_ticket, Command("ticket"))