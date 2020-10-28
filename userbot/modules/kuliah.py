from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.matkul(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    chat = "@unsiq_bot"  # pylint:disable=E0602
    matakuliah = f"matakuliah"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@unsiq_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=458359369))
            await conv.send_message(f'/{matakuliah}')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @ unsiq_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@register(outgoing=True, pattern=r"^\.passwd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    chat = "@unsiq_bot"  # pylint:disable=E0602
    password = f"password"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@unsiq_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=458359369))
            await conv.send_message(f'/{password}')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @ unsiq_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@register(outgoing=True, pattern=r"^\.idtele(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    chat = "@unsiq_bot"  # pylint:disable=E0602
    cekid = f"cekid"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@unsiq_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=458359369))
            await conv.send_message(f'/{cekid}')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @ unsiq_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(httpheader, response.message.message)


@register(outgoing=True, pattern=r"^\.dis(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    chat = "@unsiq_bot"  # pylint:disable=E0602
    dis = f"dis"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@unsiq_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=458359369))
            await conv.send_message(f'DIS (Id) (komentar)')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @ unsiq_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(httpheader, response.message.message)

CMD_HELP.update({
    "kuliah":
    "`.matkul`\
\nUsage: Untuk menampilkan mata kuliah.\
\n\n`.passwd`\
\nUsage: untuk mengganti password e-learning.\
\n\n`.idtele`\
\nUsage: untuk cek id telegram .\
\n\n`.dis`\
\nUsage: untuk komentar DIS (NOMER) ."
})
