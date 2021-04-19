import discord
from discord.ext import commands
import asyncio
import os

class Userlist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userlist(self, ctx):
        text = "名前,表示名,ID,作成日,参加日\n"
        for member in ctx.guild.members:
            if not member.bot:
                text = f"{text}{member.name},{member.display_name},{member.id},{member.created_at},{member.joined_at}\n"

        print(text)
        with open('userlist.txt','ab') as f:
            b = text.encode('cp932', 'backslashreplace')
            f.write(b)

        await ctx.author.send(file=discord.File("userlist.txt"))
        os.remove('userlist.txt')

def setup(bot):
    bot.add_cog(Userlist(bot))
