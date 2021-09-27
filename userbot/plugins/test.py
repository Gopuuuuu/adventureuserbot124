    
#Credit To @Kraken_The_BadASS . Keep credit if you are going to edit it. Join @HellBot_Official


import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="test ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
       
        await event.edit("`Testing 𝕄𝔸𝔽𝕀𝔸 𝕌𝕊𝔼ℝ𝔹𝕆𝕋....`")
        await asyncio.sleep(2)
        await event.edit("`Testing 𝕄𝔸𝔽𝕀𝔸 𝕌𝕊𝔼ℝ𝔹𝕆𝕋..`")
        await asyncio.sleep(2)
        await event.edit("__Testing Successful__")
        await asyncio.sleep(2)
        await event.edit("`Making Output` \n\nPlease wait")
        await asyncio.sleep(2)
        await event.edit("__Output Successful__")
        await asyncio.sleep(3.5)
        await event.edit("Your[𝕄𝔸𝔽𝕀𝔸 𝕌𝕊𝔼ℝ𝔹𝕆𝕋](https://t.me/MAFIA_USERBOT) is working Fine...\n       Join @MAFIA_USERBOT For Any Help......")
