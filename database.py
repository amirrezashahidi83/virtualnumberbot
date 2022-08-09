import motor.motor_tornado


class DbHelper:
    def __init__(self):
        self.client = motor.motor_tornado.MotorClient('localhost', 27017)
        self.users = self.client['users']

    
    async def insertUser(self,username):
    	document = {username:username}
    	if self.getUser(username):
    		return -1

    	return await self.users.insert_one(document)

    async def removeUser(self,username):
    	return self.users.delete_one({'username':username})
    
    async def getUser(self,username):
    	return self.users.find_one({'username':username})

    async def charge(self,username,money):
    	return self.users.update_one({'username':username},{'money':money})

