from discord.ext import commands
import discord

# コグとして用いるクラスを定義。
class Restart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #役職変更
    #イベントハンドラ使うときはclientがself.botでいいぽい。discord.ext.commands.bot以下
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def restart(self, ctx):
        await self.bot.logout()


# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(Restart(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する