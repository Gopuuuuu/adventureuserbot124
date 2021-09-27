#This plugin made by 𝕄𝔸𝔽𝕀𝔸 𝕌𝕊𝔼ℝ𝔹𝕆𝕋 owner @H1M4N5HU0P

"""Fun plugin

\nCode by @H1M4N5HU0P

type `.sorry` to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="sorry ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("╔═══╦═══╦═══╦═══╦╗──╔╗\n║╔═╗║╔═╗║╔═╗║╔═╗║╚╗╔╝║\n║╚══╣║─║║╚═╝║╚═╝╠╗╚╝╔╝\n╚══╗║║─║║╔╗╔╣╔╗╔╝╚╗╔╝\n║╚═╝║╚═╝║║║╚╣║║╚╗─║║\n╚═══╩═══╩╝╚═╩╝╚═╝─╚╝")