# Telegram-Bot-Push-Message
## How to use it
Talk to bot father, https://telegram.me/BotFather, and send message `/newbot` to create a new bot, follow the instruction, once done, you will get a token
### install the required module (in terminal)
1. `pip install telegram-send` to install the required module
2. `telegram-send --configure` to link to your created bot
#### Then insert the token that you got from bot father, press enter, obtain the passcode from the terminal and send it via the created bot in Telegram chat
#### Done! Run the codes below to send message

<br>

## Result
### Send text message
Send multiple text messages separately, an item in a list represents a message.
```
telegram_send.send(messages=["Message 1", "Message 2"])
```
<img src="readme_imgs/1.png" width="400">

<br>

### Send image message
The image will be imported from local machine, open it as a binary format.
```
with open("./files/image.jpg", "rb") as image:
  telegram_send.send(images=[image])
```
<img src="readme_imgs/2.png" width="400">

<br>

### Send a text message and image as a file with caption
You may combine few things with different formats into a single message, such as text, file, image with caption, sticker and so on.
```
with open("./files/image.jpg", "rb") as image:
    telegram_send.send(messages=["Hey!\nThis is a new message!"], files=[image], captions=["This is a image!"])
```
<img src="readme_imgs/3.png" width="400">

<br>

### Send a text file with caption
To send text and file in a single message, you may use "caption" to send the description that attached with the file.
```
with open("./files/simon_github.txt") as text_file:
    telegram_send.send(files=[text_file], captions=["This is a text file!"])
```
<img src="readme_imgs/4.png" width="400">

<br>

### Overview
<img src="readme_imgs/0.png" width="400">
