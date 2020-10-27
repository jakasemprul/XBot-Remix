from time import sleep

from userbot.events import register


@register(outgoing=True, pattern='^.cheat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Mwahahaha...Heroku mu aku cheat ya..😆😆`")
    sleep(3)
    await typew.edit("`Proses....`")
    sleep(1)
    await typew.edit("**HEROKU ANDA UDAH UNLIMITED BOSS,😎😎**")
# Create by myself @localheart


@register(outgoing=True, pattern='^.unli(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("**SISA HEROKU ANDA = UNLIMITED😎😎**")

# Create by myself @localheart
