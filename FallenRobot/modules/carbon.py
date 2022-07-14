from pyrogram.types import Message
from pyrogram import filters
from FallenRobot import pbot
from FallenRobot.utils.errors import capture_err
from FallenRobot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴀʀʙᴏɴ from 「 sᴜᴋᴜɴ ☯︎ ʀᴏʙᴏᴛ 」.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴀʀʙᴏɴ from 「 sᴜᴋᴜɴ ☯︎ ʀᴏʙᴏᴛ 」.`")
    m = await message.reply_text("😴`ɢᴇɴᴇʀᴀᴛɪɴɢ ᴄᴀʀʙᴏɴ.from 「 sᴜᴋᴜɴ ☯︎ ʀᴏʙᴏᴛ 」..`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`ᴜᴩʟᴏᴀᴅɪɴɢ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴀʀʙᴏɴ ᴛʜʀᴏᴜɢʜ 「 sᴜᴋᴜɴ ☯︎ ʀᴏʙᴏᴛ 」...`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


__mod_name__ = "Cᴀʀʙᴏɴ"

__help__ = """

ᴍᴀᴋᴇs ᴀ ᴄᴀʀʙᴏɴ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ. by 「 sᴜᴋᴜɴ ☯︎ ʀᴏʙᴏᴛ 」

❍ /carbon *:* ᴍᴀᴋᴇs ᴄᴀʀʙᴏɴ ɪғ ʀᴇᴩʟɪᴇᴅ ᴛᴏ ᴀ ᴛᴇxᴛ

 """
