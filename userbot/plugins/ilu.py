"""Fun pligon...for HardcoreUserbot

\nCode by @Kraken_The_BadASS

type `.ilu` to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="ilu ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("╔══╗╔╗╔═╦╗─╔╦═╗╔═╦╦═╦╦╗\n╚║║╝║║║║║╚╦╝║╦╝╚╗║║║║║║\n╔║║╗║╚╣║╠╗║╔╣╩╗╔╩╗║║║║║\n╚══╝╚═╩═╝╚═╝╚═╝╚══╩═╩═╝")