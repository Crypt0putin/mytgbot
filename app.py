from telethon import TelegramClient, events

BOT_TOKEN = '1331311772:AAG_-VZakzFr0pcZuAzRJvKUqbcJpsfBgj8'
API_ID = 2678631
API_HASH = 'b26fa1479454694c0b70dacdc1484f58'

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('Привет! Я бот-попугай, повторяю твои сообщения)')
    raise events.StopPropagation

@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message."""
    await event.respond(event.text)

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()