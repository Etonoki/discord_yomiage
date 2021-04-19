import json
from discord.ext import commands
import discord
import requests
import sys

send_data = {
    'apikey' : 'DZZdyPAWywwXd6qQZsZKPSuX93etbd8q',
    'query' : ''
}

class Talk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        #よくわからんからメンションを色々して外してる
        if self.bot.user in message.mentions:
            send_data['query'] = message.content.strip("<@639495712635093015>")
            #空文字排除
            if send_data['query'] != "":
                #とりエラー処理しないとポートでエラーが酷い。なお治ってない模様。マルチスレッドやめてmainのrunでポート指定する必要あり。kwskはErrorR10で検索
                try:
                    #https://devcenter.heroku.com/articles/error-codes#r10-boot-timeout
                    r = requests.post("https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk", data=send_data,  timeout=5.0)
                    return_data = r.json()
                    response = return_data['results'][0]['reply']
                    await message.channel.send(message.author.mention + " " + response)
                except Exception:
                    print('request failed')

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(Talk(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。