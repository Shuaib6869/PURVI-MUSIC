from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SACHIN_MUSIC import app
from config import BOT_USERNAME
from SACHIN_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - 𝗩𝗜𝗟𝗟𝗔𝗜𝗡
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - KYA KROGE JANKE
│├─────────────────╯
├┼─────────────────⦿
├┤~ @NoT_YoUr_ViLLain
├┤~ @LEGEND_HU_BSDK
├┤~ @PARDHAN_HU_BSDK
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @LEGEND_HU_BSDK
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton(" 𝗟𝗘𝗚𝗘𝗡𝗗 ", url=f"https://t.me/LEGEND_HU_BSDK")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/VILLAIN_MUSIC_UPDATE"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://t.me/VILLAIN_MUSIC_UPDATE"),
          ],
               [
                InlineKeyboardButton("VILLAIN ɴᴇᴛᴡᴏʀᴋ", url=f"https://t.me/VILLAIN_MUSIC_UPDATE"),
],
[
InlineKeyboardButton("ᴏғғɪᴄɪᴀʟ ʙᴏᴛ", url=f"https://t.me/ViLLaiN_Music_bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/0wtv2m.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
