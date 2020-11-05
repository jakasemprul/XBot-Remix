from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.pay(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("📱DANA 085877240759 📱PULSA 082114264663")
# Create by myself @localheart


@register(outgoing=True, pattern='^.list(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("SSH INDO 🇮🇩 10 K   SSH SG 🇨🇱 15 K")
# Create by myself @localheart


@register(outgoing=True, pattern='^.jual(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("https://telegra.ph/file/b73721b40100fc93bc9d6.jpg")
# Create by myself @localheart


CMD_HELP.update({
    "harga":
    "`.pay`\
\nUsage: Nomer Telepon dan DANA\
\n\n`.list`\
\nUsage:List harga ssh\
\n\n`.jual\
 \nUsage: Daftar jualan.\"
})
