from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER




class Zoro(Client):
    def __init__(self):
        LOGGER("ميــوزك جاكو").info(f"جارِ بدء تشغيل البوت . . .")
        super().__init__(
            name="VeGaMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» تم تشغيل الميـوزك لـ البوت {self.mention} :</b><u>\n\n- ɪᴅ : <code>{self.id}</code>\n- ɴᴀᴍᴇ : {self.name}\n- ᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "» قم باضافة البـوت مشـرفـاً بكافة الصلاحيات في مجموعـة السجـل"
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}."
            )
            exit()

        LOGGER("ميــوزك جاكو").info(f" تم بدء تشغيل البوت {self.name} ...✓")

    async def stop(self):
        await super().stop()