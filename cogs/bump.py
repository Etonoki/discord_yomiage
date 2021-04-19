import discord
from discord.ext import commands
import asyncio

class Bump(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ###bump通知
    @commands.Cog.listener()
    async def on_message(self,message):
        #bump通知用
        if message.author.id == 302050872383242240:
            embed_list = message.embeds[0].to_dict()
            #色で判定（エラーは15420513）
            if embed_list['color'] == 2406327:
                await asyncio.sleep(7200)
                bump_role = discord.utils.get(message.guild.roles, name="bump")
                await message.channel.send(f"bumpできるよ！")

    '''
    ###bumpロール着脱
    @commands.command()
    async def bump(self, ctx):
        bump_role = discord.utils.get(ctx.guild.roles, name="bump")
        if bump_role in ctx.author.roles:
            await ctx.author.remove_roles(bump_role)
            msg = await ctx.send("ロールを解除しました。")
        else:
            await ctx.author.add_roles(bump_role)
            msg = await ctx.send("ロールを付与しました。\n``/bump``で設定を解除できます。")
        await asyncio.sleep(5)
        await msg.delete()
    '''


def setup(bot):
    bot.add_cog(Bump(bot))
