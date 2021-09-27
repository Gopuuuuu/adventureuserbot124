import asyncio
import os
import shlex
from os import getcwd
from os.path import basename, joinfrom textwrap import wrap
from typing import Optional, Tuple import numpy as np
from PIL import Image, ImageDraw, ImageFont
from telethon.errors.rpcerrorlist import YouBlockedUserError




async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )