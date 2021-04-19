import discord
from discord.ext import commands
import asyncio
import os
import json

class Userlist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userlist(self, ctx):
        text = "名前,表示名,ID,作成日,参加日\n"
        print(ctx.guild.members)
        for member in ctx.guild.members:
            print("2")
            if not member.bot:
                print("1")
                text = f"{text}{member.name},{member.display_name},{member.id},{member.created_at},{member.joined_at}\n"

        print(text)
        with open('userlist.txt','ab') as f:
            b = text.encode('cp932', 'backslashreplace')
            f.write(b)

        await ctx.author.send(file=discord.File("userlist.txt"))
        os.remove('userlist.txt')

    @commands.command()
    async def userlist1(self, ctx):
        #windowsなのでエンコード
        json_open = open('speakUser.json', 'r', encoding="utf-8_sig")
        json_load = json.load(json_open)
        await ctx.send(json_load)


def setup(bot):
    bot.add_cog(Userlist(bot))
