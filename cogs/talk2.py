import json
from discord.ext import commands
import discord
#import aiohttp
import requests

send_data = {
    "utterance": "",
    "username": "",
    "agentState":{
        "agentName": "私",
        "tone": "normal",
        "age": "20歳"
    }
}

#https://qiita.com/maKunugi/items/b1afb6441571119729a7

class Talk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        #よくわからんからメンションを色々して外してる
        # or message.channel.id == チャンネルIDでそこで
        if self.bot.user in message.mentions or isinstance(message.channel, discord.DMChannel):
            send_data['utterance'] = message.content.strip("<@639495712635093015>")
            send_data['username'] = message.author.name 
            #空文字排除
            if send_data['utterance'] == "":
                return
            '''
            async with aiohttp.ClientSession() as session:
                async with session.post("https://www.chaplus.jp/v1/chat?apikey=5e6cc47913d64",json=send_data) as r:
                    print(r)
                    if r.status == 200:
                        print(r.json())
                        card = await r.json()
                        res = card["bestResponse"]['utterance']
                        await message.channel.send(message.author.mention + " " + res)
                    else:
                        await message.channel.send("エラーですよ！！！！！！！！！！！！！！！！")
            '''
            #https://devcenter.heroku.com/articles/error-codes#r10-boot-timeout
            r = requests.post("https://www.chaplus.jp/v1/chat?apikey=5e6cc47913d64", json=send_data,  timeout=5.0)
            return_data = r.json()
            response = return_data['bestResponse']['utterance']
            await message.channel.send(message.author.mention + " " + response)



# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(Talk(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。