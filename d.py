class Email:
    @staticmethod
    def send_email():
        pass
        
        

class Sms:
    @staticmethod
    def send_sms():
        pass


class Notification:
    def __init__(self, name: str):
        self.email = Email()
        self.sms = Sms()
    
    def send(self):
        self.email.send_email()
        self.sms.send_sms()
        






#------------------

from abc import ABC, abstractmethod


class Message(ABC):
    @abstractmethod
    def send(self):
        pass

class Email(Message):
    def send(self):
        pass
        
        

class Sms(Message):
    def send(self):
        pass

class Notification:
    def __init__(self, messages):
        self.messages = messages
        
    def send(self):
        for message in self.messages:
            message.send()