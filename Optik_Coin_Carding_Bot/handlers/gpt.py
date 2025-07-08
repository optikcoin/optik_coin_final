from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
import aiohttp
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Set your OpenAI API key as an environment variable

async def gpt_query(message: types.Message):
    prompt = message.get_args()
    if not prompt:
        await message.reply("Please provide a prompt. Example: /gpt What is AI?")
        return

    if not OPENAI_API_KEY:
        await message.reply("OpenAI API key not set.")
        return

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as resp:
            if resp.status == 200:
                data = await resp.json()
                reply = data["choices"][0]["message"]["content"].strip()
                await message.reply(reply)
            else:
                await message.reply("Error communicating with OpenAI API.")

def register_gpt_handler(dp: Dispatcher):
    dp.register_message_handler(gpt_query, Command("gpt"))