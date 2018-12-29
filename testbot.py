#!/usr/bin/python3.6
import telepot
import time
import urllib3

# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts

bot = telepot.Bot('725961562:AAF_q7ncRxHoxhgXVIhCr1Il8KhyPB0TzwM')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if msg['text']=='/start' :
            bot.sendMessage(chat_id,'سلام دوست من. به ربات من خوش اومدی اینجا میتونی هرچی دلت بخوای بهم بگی بدون اینکه خودتی معرفی کنی.      ممنون میشم نظرتو بهم بگی ')
        else:
            bot.sendMessage('212490589', "a person said '{}'".format(msg["text"]))

bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
