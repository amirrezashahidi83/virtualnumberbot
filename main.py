import api
import database
import pyrogram
import payment
import panels
from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import (ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardButton,InlineKeyboardMarkup)
import json

language_file = open("language.json","r", encoding='utf-8')
language_json = json.loads(language_file.read())
language_file.close()


api_id = 3529684
api_hash = "2c16080732e86a559fa05b20ff02acb8"
token_bot = "5544674447:AAH8FRt69CMpzsqK6IFQxT8PzO9bVnqEyuc"

proxy = {
     "scheme": "http",
     "hostname": "192.168.1.3",
     "port": 59225,
}

client = pyrogram.Client('session.sh',api_id=api_id,api_hash=api_hash,bot_token=token_bot,proxy=proxy)

apihelper = api.ApiHelper()

dbhelper = database.DatabaseHelper()

async def Support(client,user_id):
    await client.send_message(user_id,"i")

async def sendAffilateLink(user_id):
    await client.send_message(user_id,"link")

async def addAffilate(user_id,merchant_id):
    dbhelper.insertAffilate(user_id,merchant_id)

    await client.send_message(user_id,"d")

async def start(client,message):

    user_id = message.from_user.id
    if message.command[1]:
        addAffilate(message.from_user.id,message.command[1])

    if dbhelper.insertUser(user_id) == -1:
        await client.send_message(user_id,language_json['Messages']['hasStarted'])
    else:
        await client.send_message(user_id,language_json['Messages']['successStart'])

client.add_handler(MessageHandler(start,filters.command(['start'])))
print("started...")
client.run()
