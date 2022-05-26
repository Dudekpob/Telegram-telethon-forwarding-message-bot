from telethon import TelegramClient, events
import asyncio
api_id = ''
api_hash = ''
client = TelegramClient('none', api_id, api_hash)
@client.on(events.NewMessage)
async def handler(event):
        async for dialog in client.iter_dialogs():
          if dialog.is_channel:
           print(f'{dialog.id}:{dialog.title}')

client.start()
client.run_until_disconnected()
