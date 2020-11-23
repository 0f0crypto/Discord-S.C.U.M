'''
if someone replies to your message in a dm, this code will use a recent bug to give that person the SERVER badge (credits go to https://github.com/divinityseraph/server-badge-exploit)
here's how it looks: https://www.reddit.com/r/discordapp/comments/jzlnlb/discords_new_reply_feature_is_fun_and_bugged_lol/
this bug works both on servers and DMs :)
'''

import requests, json #cause this bugged endpoint is not in discum yet, will update later

import discum
import time

bot = discum.Client(token='ur token')

@bot.gateway.command
def helloworld(resp):
    if resp['t'] == "READY_SUPPLEMENTAL": #ready_supplemental is sent after ready
        user = bot.gateway.SessionSettings.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
    if resp['t'] == "MESSAGE_CREATE":
        m = resp['d']
        if m['content'] == 'turn me into a server':
            bot.sendMessage(m['channel_id'], 'reply to one of my messages and I will make you a server :)')
        if m['author']['id'] == ':
            return
        if m['type'] == 19:
            if 'referenced_message' in m and m['referenced_message']['author']['id'] == bot.gateway.SessionSettings.user['id'] and 'guild_id' not in m:
                time.sleep(1) instant replies make ppl think ur running a selfbot so...
                channelID = m['channel_id']
                baseURL = "https://discord.com/api/channels/{}/messages".format(channelID)
                POSTedJSON =  json.dumps ({"content":"The server Gods have allowed me to grant you the server badge. You are now a server :).","nonce":None,"tts":False,"message_reference":{"guild_id":None,"channel_id":m['channel_id'],"message_id":m['id']},"allowed_mentions":{"parse":["users","roles","everyone"],"replied_user":False}})
                try:
                    bot.s.post(baseURL, data=POSTedJSON)
                except:
                    bot.s.post(baseURL, data=POSTedJSON)
                time.sleep(2) #instant replies make ppl think ur running a selfbot so...

bot.gateway.run()
