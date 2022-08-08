import requests
import json
class ApiHelper:
    def __init__(self):
        self.url = 'http://api.numberland.ir/v2.php/?apikey=9ff5eea4fbcf9d6123644c86a34ce55d&method='
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def getCountries(self):
        response = requests.get(self.url+"getcountry",headers=self.headers)
        return json.loads(response.text)

    def getServices(self):
        response = requests.get(self.url+"getservice",headers=self.headers,verify=False)
        return json.loads(response.text)

    def getNumbers(self):
        response = requests.get(self.url+'getinfo',headers=self.headers)
        return json.loads(response.text)
    
    def getNumbersByService(self,service):
        response = requests.get(self.url+'getinfo&service='+str(service),headers=self.headers)
        return json.loads(response.text)
    
    def getBalance(self):
        response = requests.get(self.url+'balance',headers=self.headers);
        return json.loads(response.text)

    def checkStatus(self,_id):
        response = requests.get(self.url+'checkstatus&id='+str(_id),headers=self.headers)
        return json.loads(response.text)

    def buyNumber(self,country,operator,service):
        response = requests.get(self.url+'getnum&country='+country+"&operator="+operator+"&service="+service,headers=self.headers)
        return json.loads(response)

    def cancelNumber(self,_id):
        response = requests.get(self.url+'cancelnumber&id='+_id);
        return json.loads(response)

    def banNumber(self,_id):
        response = requests.get(self.url+'bannumber&id='+_id)
        return json.loads(response)

    def repeat(self,_id):
        response = requests.get(self.url+'repeat&id='+_id)
        return json.loads(response)

    def closeNumber(self,_id):
        response = requests.get(self.url+'closenumber&id='+_id)
        return json.loads(response)