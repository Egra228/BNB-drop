from pyrogram import Client, filters
import time

api_id = Change
api_hash = 'Change'

app = Client('Account', api_id, api_hash)

while True:
    with app:
        app.send_message('@oxbnb_bot','🎁')
        time.sleep(600)

app.start()


