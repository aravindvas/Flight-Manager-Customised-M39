from twilio.rest import Client
import os

tw_id = "AC405565638eb21752d664f91e7c1c16ce"
tw_tkn = "3685d4c70f1f0aa0cef968c2c586d4d2"
tw_no = "+19256432125"
my_no = "+919491654127"

class Notification():

    def __init__(self):
        self.client = Client(tw_id, tw_tkn)

    def sms(self, msg2):
        msg = self.client.messages.create(
            body=msg2,
            from_=tw_no,
            to=my_no
        )
        print(msg.sid, msg.status)