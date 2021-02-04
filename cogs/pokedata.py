from discord.ext import commands
import discord
import json
from discord import embeds
import urllib.request
import math

#更新が必要な画像ファイル
#https://github.com/fanzeyi/pokemon.json
#データ
#https://github.com/kotofurumiya/pokemon_data
#埋め込みヘルプ
#https://discordpy.readthedocs.io/ja/latest/faq.html#how-do-i-use-a-local-image-file-for-an-embed-image

#JSON ファイルの読み込み
f = urllib.request.urlopen('https://raw.githubusercontent.com/kotofurumiya/pokemon_data/master/data/pokemon_data.json').read()
json_data = json.loads(f.decode('utf-8'))

class Pokedata(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poke(self, ctx, arg):
        for data in json_data:
            if data["name"] == arg:
                ttt = ""
                uuu = ""
                vvv = ""
                n = 1
                m = 1
                for aaa in data["types"]:
                    ttt = "{}タイプ{} : {}\n".format(ttt,n,aaa)
                    n = n + 1
                for aaa in data["abilities"]:
                    uuu = "{}特性{} : {}\n".format(uuu,m,aaa)
                    m = m + 1
                if data["hiddenAbilities"]:
                    uuu = "{}夢特性 : {}\n".format(uuu,data["hiddenAbilities"][0])
                if data["form"]:
                    vvv = "（{}）".format(data["form"])

                #ローカル出力はherokuで出来ない
                embed=discord.Embed(color=0xff40ff)
                embed.set_author(name="{:0=3} : {}{}".format(data['no'],data['name'],vvv),icon_url="https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/sprites/{:0=3}MS.png".format(data["no"]))
                embed.add_field(name="**〇タイプ**", value=ttt ,inline=True)
                embed.add_field(name="**〇特性**", value=uuu ,inline=True)
                embed.set_image(url="https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/{:0=3}.png".format(data["no"]))
                embed.add_field(name="**〇種族値**",
                    value="HP : " + str(data['stats']['hp']) + 
                    "\n攻撃 : " + str(data['stats']['attack']) + 
                    "\n防御 : " + str(data['stats']['defence']) + 
                    "\n特攻 : " + str(data['stats']['spAttack']) + 
                    "\n特防 : " + str(data['stats']['spDefence']) + 
                    "\n素早さ : " + str(data['stats']['speed']),inline=True)

                await ctx.channel.send(embed=embed)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(Pokedata(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。