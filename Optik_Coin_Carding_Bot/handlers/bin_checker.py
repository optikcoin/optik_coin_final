from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
import aiohttp

async def bin_lookup(message: types.Message):
    args = message.get_args()
    if not args or not args.isdigit() or len(args) < 6:
        await message.reply("Please provide a valid BIN (at least 6 digits). Example: /bin 45717360")
        return

    bin_number = args[:8]  # Most BINs are 6-8 digits
    url = f"https://lookup.binlist.net/{bin_number}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                info = (
                    f"**BIN:** {bin_number}\n"
                    f"**Scheme:** {data.get('scheme', 'N/A')}\n"
                    f"**Type:** {data.get('type', 'N/A')}\n"
                    f"**Brand:** {data.get('brand', 'N/A')}\n"
                    f"**Bank:** {data.get('bank', {}).get('name', 'N/A')}\n"
                    f"**Country:** {data.get('country', {}).get('name', 'N/A')}\n"
                )
                await message.reply(info, parse_mode="Markdown")
            else:
                await message.reply("BIN not found or API error.")

def register_bin_checker(dp: Dispatcher):
    dp.register_message_handler(bin_lookup, Command("bin"))