import simplematrixbotlib as botlib

creds = botlib.Creds(
    homeserver="",
    username="",
    password="",
)
bot = botlib.Bot(creds=creds)
PREFIX = '!'


@bot.listener.on_message_event
async def echo(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("echo"):

        await bot.api.send_text_message(
            room.room_id, " ".join(arg for arg in match.args())
            )

bot.run()
