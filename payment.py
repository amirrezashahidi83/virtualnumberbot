import requests
import json

class Payment:

	def __init__(self):
		self.url = "https://api.idpay.ir/v1.1/payment"
		self.callback = ""

	def createPayment(amount):
		parameters = {
			'order_id':1,
			'amount':amount,
			'callback':self.callback
		}
		response = requests.post(self.url,data=parameters)
		callback_data = json.loads(response.text)
		_id = callback_data['id']
		link = callback_data['link']