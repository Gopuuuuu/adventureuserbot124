import asyncio
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, mafiaversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ππΈπ½ππΈ πππΌβπΉππ"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

PM_IMG = "https://telegra.ph/file/b61486075c6ef73dd0d12.png"
pm_caption = "__**π₯π₯ππΈπ½ππΈ πππΌβπΉππ ππ πΈππππΌπ₯π₯**__\n\n"

pm_caption += f"               πππΈπππΌβπ\n**γ[{DEFAULTUSER}](tg://user?id={mafia})γ**\n\n"

pm_caption += "π‘οΈTELETHONπ‘οΈ : `1.15.0` \n"

pm_caption += f"π`β° πΈππ§πππ₯π¦π£π β° πππΌβπΉπππ       : `{mafiaversion}`\n"

pm_caption += f"π±Sudoπ±            : `{sudou}`\n"

pm_caption += "πCHANNELποΈ   : [α΄α΄ΙͺΙ΄](https://t.me/adventure_family)\n"

pm_caption += "πCREATORπ    : [gopal](@teri_behn_ka_bf)\n\n"

pm_caption += "π€©SUPPORTERπ€©    :[HellBoy](@export_gabber)\n\n"

pm_caption += "      [β¨REPOβ¨](https://github.com/Gopuuuuu/adventureuserbot.git) πΉ [πLicenseπ](https://github.com/H1M4N5HU0P/MAFIA-USERBOT/blob/main/LICENSE)"
#@command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
