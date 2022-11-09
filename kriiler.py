from pypresence import Presence
import time
import json

with open('secret_stuff.json') as secret_stuff:
    keys = json.loads(secret_stuff.read())
with open('tm.json') as tm:
    data = json.loads(tm.read())

client_id = keys['client_id'] #Put your client ID here
RPC = Presence(client_id) 
RPC.connect() 

RPC.update(
    state=data['state'], 
    details=data['details'], 
    large_image=data['large_image'], 
    small_image=data['small_image'], 
    large_text=data['large_text'], 
    small_text=data['small_text'],
    party_size=[data['party_size'], data['party_max']],
    buttons=[
                {"label":data['label1'],"url":data['url1']},
                {"label":data['label2'],"url":data['url2']}
            ],
    start=time.time())

while True: 
    time.sleep(15) 