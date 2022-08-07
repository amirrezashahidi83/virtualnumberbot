import api
import database
import pyrogram
from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import (ReplyKeyboardMarkup, KeyboardButton)
import json

language_file = open("language.json","r")
language_json = json.loads(language_file.read())
language_file.close()

print(language_json['buynumber'])

api_id = 3529684
api_hash = "2c16080732e86a559fa05b20ff02acb8"
token_bot = "5544674447:AAH8FRt69CMpzsqK6IFQxT8PzO9bVnqEyuc"

proxy = {
     "scheme": "socks5",
     "hostname": "127.0.0.1",
     "port": 3000,
}

client = pyrogram.Client('session.sh',api_id=api_id,api_hash=api_hash,bot_token=token_bot,proxy=proxy)

async def showPanel(client,user_id):
	await client.send_message(
		user_id,
		"jk",
		reply_markup=ReplyKeyboardMarkup(
                [
                	['خرید شماره مجازی']
                ]
            ))

async def start(client,message):
	await showPanel(client,message.from_user.id);

client.add_handler(MessageHandler(start,filters.command(['start'])))
print("started...")
client.run()