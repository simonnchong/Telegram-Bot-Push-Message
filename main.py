# talk to bot father, https://telegram.me/BotFather, and send message `/newbot` 
# to create a new bot, follow the instruction, once done, you will get a token
# install the required module (in terminal)
#* 1. `pip install telegram-send`
# link the module to your created bot
#* 2. type `telegram-send --configure`, then insert the token that you got from bot father, press enter
# obtained code from the terminal and send it via the created bot in telegram
# done! Run the codes below to send message

import telegram_send

# # send text message
telegram_send.send(messages=["Message 1", "Message 2"]) # an item in a list represent a message

# send image message
with open("./files/image.jpg", "rb") as image: # insert your own image path here, read the file as binary mode
    telegram_send.send(images=[image]) # an item in a list represent a message
    
# send a text message and image as a file with caption
with open(".files/image.jpg", "rb") as image: # insert your own image path here, read the file as binary mode
    telegram_send.send(messages=["Hey!\nThis is a new message!"], files=[image], captions=["This is a image!"]) 

# send a text file with caption
with open(".files/simon_github.txt") as text_file: # insert your own text file path here
    telegram_send.send(files=[text_file], captions=["This is a text file!"]) 
    

# NOTE you can send any other format via this API by using different parameters
# send(*, messages=None, files=None, images=None, stickers=None, animations=None, videos=None, audios=None, captions=None, locations=None, conf=None, parse_mode=None, pre=False, silent=False, disable_web_page_preview=False, timeout=30)

# NOTE telegram_send documentation: https://pypi.org/project/telegram-send/ 
# NOTE reference: https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580