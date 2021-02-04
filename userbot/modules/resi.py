
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.resi(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    chat = "@cekresionline_bot"  # pylint:disable=E0602
    resi = f"resi"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@cekresionline_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1426594594))
            await conv.send_message(f'{kode_ekspedisi} {nomor_resi}')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @ cekresionline_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


CMD_HELP.update({
    "resi":
    "`.resi`\
\nUsage: Cek resi \
\n\n`.lacak`\
\nUsage:lacak paket"
})
