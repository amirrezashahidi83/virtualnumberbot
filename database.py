import motor.motor_tornado


class DbHelper:
    def __init__(self):
        self.client = motor.motor_tornado.MotorClient('localhost', 27017)
        

        
        
