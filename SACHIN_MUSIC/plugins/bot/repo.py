from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SACHIN_MUSIC import app
from config import BOT_USERNAME
from SACHIN_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
⌾ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ ɪɴᴄʀɪᴄɪʙʟᴇ ʀᴇᴘᴏs ⌾
 
◎ ʙʜᴀɢ ʙʜᴏsᴅɪᴋᴇ
 
◎ ʀᴇᴘᴏ ᴛᴏ ɴᴀ ᴅᴜɴɢᴀ
"""




@app.on_message(filters.command("mmrepo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴇʟᴘ •", url="https://t.me/FRIENDS_CHATTING_ZONE_II"),
          InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/LEGEND_HU_BSDK"),
          ],
               [
                InlineKeyboardButton("• VILLAIN ɴᴇᴛᴡᴏʀᴋ •", url=f"https://t.me/@VILLAIN_MUSIC_UPDATE"),
],
[
InlineKeyboardButton("• ᴏғғɪᴄɪᴀʟ ʙᴏᴛ •", url=f"https://t.me/ViLLaiN_Music_bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/0wtv2m.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
