
"""
.kickme
"""
from telethon.tl.functions.channels import LeaveChannelRequest
from userbot.utils import admin_cmd
import time

@borg.on(admin_cmd("kickme", outgoing=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("**My Master Bored Here Bye Bye Guys?**")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('**This Command Only Use In Groups**')
