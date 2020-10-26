from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.pay(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("DANA 085877240759 PULSA 082114264663")
# Create by myself @localheart
