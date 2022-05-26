from telethon import TelegramClient, events
import asyncio

Id_Group1 = x
Id_Group2 = x
Id_Group3 = -x
Id_Group4 = -x
Id_Group5 = -x
Id_Group6 = -x
Id_Group7 = -x
Id_Group8 = -x
Id_Group9 = -x
Id_Group10 = -x
Id_Group11 = -x
Id_Group12 = -x
Id_Group13 = -x
Id_Group14 = x
Id_Group15 = x
Id_Group16 = x

api_id = ''
api_hash = ''
client = TelegramClient('none', api_id, api_hash)
@client.on(events.NewMessage)
async def handler(event):
    chat = await event.get_chat()
    chat_id = event.chat_id
    print(chat_id)

    if chat_id == Id_Group3 or chat_id == Id_Group4 or chat_id == Id_Group5   or chat_id == Id_Group6 or chat_id ==Id_Group7 or chat_id == Id_Group8  or chat_id ==Id_Group9 or chat_id ==Id_Group10 or chat_id == Id_Group11 or chat_id == Id_Group12 or chat_id == Id_Group13 or chat_id == Id_Group14 or chat_id == Id_Group15 or chat_id == Id_Group16: 
        await client.send_message(Id_Group1, event.raw_text)
        await client.send_message(Id_Group2, event.raw_text)
       

client.start()
client.run_until_disconnected()
