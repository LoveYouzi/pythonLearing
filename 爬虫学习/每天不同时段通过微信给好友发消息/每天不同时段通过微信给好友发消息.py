import configparser
import requests
from wxpy import *
import itchat

# 获取每日精句
def get_message():
    message = requests.get('http://open.iciba.com/dsapi/')
    note = message.json()['note']
    content = message.json()['content']
    return note,content
    #print(message.json())

def send_message(message):
    bot = Bot()
    friends = bot.friends()
    for friend in friends:
        print(friend)


if __name__ == '__main__':
    send_message(2)
    get_message()
    # cf = configparser.ConfigParser()
    # cf.read('configure.ini', "utf-8")
    # print(cf.options('configure'))
    # print(cf.get('configure','weixin_name'))