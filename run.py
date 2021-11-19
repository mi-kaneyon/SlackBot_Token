# coding: utf-8
#from slacker import Slacker
#import slackbot_settings
from slackbot.bot import Bot

def main():
 #   slack = Slacker(slackbot_setting.API_TOKEN)
 #   slack.chat.post_message("timeline", "change-message", as_user=True)
    
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    print('start slackbot')
    main()
