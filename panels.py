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
