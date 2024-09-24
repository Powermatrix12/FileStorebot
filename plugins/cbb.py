#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import *
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>POWER OWNER</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/cybermatrixXtm'>ᴄʏʙᴇʀᴍᴀᴛʀɪxᴛᴍ</a>\n○ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/powermoviespage'>ᴘᴏᴡᴇʀ ᴍᴏᴠɪᴇs</a>\n○ ᴘʀᴇᴍɪᴜᴍ ᴍᴏᴅs : <a href='https://t.me/+JjTNgj4J3_NkMWM1'>ᴘᴏᴡᴇʀ ᴍᴏᴅs</a>\n○ ᴄʜᴀᴛ ɢʀᴏᴜᴘ : <a href='https://t.me/simplebuddys'>sɪᴍᴘʟᴇ ʙᴜᴅᴅʏs</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ʜᴅᴍᴏᴠɪᴇs', url='https://t.me/+zgKTqE-TN24yZjk1')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
