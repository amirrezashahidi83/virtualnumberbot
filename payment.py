import requests
import json
import database

class PaymentHelper:

	def __init__(self):
		self.url = "https://api.idpay.ir/v1.1/payment"
		self.callback = ""
		self.headers = {
			'Content-Type':'application/json',
			'X-API-KEY':'6a7f99eb-7c20-4412-a972-6dfb7cd253a4',
			'X-SANDBOX':'1'
		}

	def createPayment(self,amount):

		parameters = {
			'order_id':1,
			'amount':amount,
			'callback':self.callback
		}
		response = requests.post(self.url,data=json.dumps(parameters),headers=self.headers)
		callback_data = json.loads(response.text)
		print(callback_data)
		_id = callback_data['id']
		link = callback_data['link']
		insertTransaction(_id,link)

		return link

	def verifyTransaction(self,_id):
		parameters = {'id':_id,'order_id':1}
		response = requests.post(self.url+'/verify',data=parameters)

		return json.loads(response);

	def checkTransaction(self,_id):
		parameters = {'id':_id,'order_id':1}
		response = requests.post(self.url+'/inquiry',data=parameters)

		return json.loads(response)

		
