# coding: utf-8
import os
from slackbot.bot import respond_to  # メンションで反応
from slackbot.bot import listen_to  # チャンネル内発言で反応
from slackbot.bot import default_reply  # 該当する応答がない場合に反応
from transformers import T5Tokenizer, AutoModelForCausalLM
import time, sys
from slackclient import SlackClient
import slackbot_settings
import requests
from slacker import Slacker
import slackweb
# from plugins import read

# T5Tokenizer AutoTokenizer
# トークナイザーとモデルの準備--you can change your tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
model = AutoModelForCausalLM.from_pretrained("model's fold path")

# hook information
SLACKURL = 'https://hooks.slack.com/services/xxxxxxxx'
SLACKUSERID = 'yourID \n'

slack_token = 'xoxb-2700210612390-2692312905431-mf78m5nUNFPvbA9OPp0nNpzT'
sc = SlackClient(slack_token)
sc.api_call(
    "chat.postMessage",
    channel="#general",
    text="@casade-san に質問してください。#generalに回答します。"
)


@default_reply()

@respond_to('(.*)')
def hello(message,something):

 
            
    slacker = Slacker(slackbot_settings.API_TOKEN)
  
    mes = message.body['text']
    input = tokenizer.encode(mes, return_tensors="pt")
    output = model.generate(input, do_sample=True, max_length=250, num_return_sequences=3)
    os.chdir('your path')
    with open('generated message name or path', 'w') as f:
        print(tokenizer.batch_decode(output),file=f) 
        channel='#general'
        
    file = 'file.txt'
    slacker.files.upload(file_=file, channels=channel)
    message.reply("@bot_name に質問してください。#generalに回答します。")
    
@listen_to("反応語句")
def listen(message):
    message.reply("返事")

@respond_to("反応語句")
def respod(message):
    message.reply("返事")

