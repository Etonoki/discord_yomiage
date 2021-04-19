from discord.ext import commands
import discord
import os
import datetime
from discord import embeds
import asyncio
import io

class ManageChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ###入力者のログ削除
    @commands.command(aliases=["del"])
    async def delete(self, ctx, arg=50):
        if arg == 0:
            arg = None
        try:
            async for msg in ctx.history(limit = arg):
                if msg.author == ctx.author:
                    await msg.delete()
        except:
            await ctx.send("バグったんで処理止めたよ！！！！！！") 
            pass

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(ManageChannel(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。