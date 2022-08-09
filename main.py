import api
import database
import pyrogram
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
     "scheme": "socks5",
     "hostname": "127.0.0.1",
     "port": 3000,
}

client = pyrogram.Client('session.sh',api_id=api_id,api_hash=api_hash,bot_token=token_bot,proxy=proxy)

apihelper = api.ApiHelper()

async def Support(client,user_id):
    await client.send_message(user_id,"i")

async def showProfilePanel(user_id):
    buttons = [] 
    
async def showNumbersPanel(user_id,service):
    buttons = [[]]
    row = 0
    allNumbers = apihelper.getNumbersByService(service)
    for number in allNumbers:
        buttons[row].append(InlineKeyboardButton(number['country'],callback_data=number['country']))
        buttons[row].append(InlineKeyboardButton(number['amount'],callback_data=number['amount']))
        if len (buttons[row]) == 2:
            buttons.append([])
            row += 1

    await client.send_message(user_id,"fds",
        reply_markup=InlineKeyboardMarkup(buttons))

async def showServicesPanel(client,user_id):
    
    buttons = [[]]
    row = 0
    servicesPanel_lang = language_json['ServicesPanel']
    allServices = apihelper.getServices()
    for service in allServices:
        buttons[row].append(InlineKeyboardButton(service['name'],callback_data=service['name']))
        if len(buttons[row]) == 3:
            buttons.append([])
            row += 1

    await client.send_message(user_id,"ta",
        reply_markup=InlineKeyboardMarkup(buttons))

async def showMainPanel(client,user_id):

    buttons =   [
                    [mainPanel_lang["buyNumberButton"],mainPanel_lang['getPrices']],
                    [mainPanel_lang["charge"],mainPanel_lang['showMyAccount']],
                    [mainPanel_lang["support"]]
                ]

	mainPanel_lang = language_json['MainPanel']
	
	await client.send_message(
		user_id,
		"jk",
		reply_markup=ReplyKeyboardMarkup(buttons))

async def start(client,message):
	await showNumbersPanel(message.from_user.id,1);

client.add_handler(MessageHandler(start,filters.command(['start'])))
print("started...")
client.run()
