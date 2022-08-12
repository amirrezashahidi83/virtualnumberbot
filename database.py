import motor.motor_tornado


class DbHelper:
    def __init__(self):
        self.client = motor.motor_tornado.MotorClient('localhost', 27017)
        self.users = self.client['users']
        self.transactions = self.client['transactions']
        self.affilates = self.client['affilates']
    
    async def insertUser(self,username):
    	document = {username:username}
    	if self.getUser(username):
    		return -1

    	return await self.users.insert_one(document)

    async def removeUser(self,username):
    	return self.users.delete_one({'username':username})
    
    async def getUser(self,username):
    	return self.users.find_one({'username':username})

    async def charge(self,username,amount):
    	return self.users.update_one({'username':username},{'money':amount})

    async def insertTransaction(self,_id,link):
    	document = {'id':_id,'link':link}
    	if self.getTransaction(_id):
    		return -1
    	return await self.transactions.insert_one(document)

    async def getTransaction(self,_id):
    	return await self.transactions.find_one({'id':_id})

    async def getAffilates(self,merchant_id):
        return await self.affilates.find({'merchant_id':merchant_id})

    async def insertAffilate(self,affilate_id,merchant_id):
        document = {'affilate_id':affilate_id,'merchant_id':merchant_id}

        for affilate in getAffilates(merchant_id):
            if affilate.affilate_id == affilate_id:
                return -1
        return await self.affilates.insert_one(document)
    