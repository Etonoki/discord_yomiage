from discord.ext import commands
import discord
from discord import embeds

# コグとして用いるクラスを定義。
class ChangeHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="TTS機能一覧", color=0xff40ff)
        embed.set_author(name=self.bot.user.name,icon_url=self.bot.user.avatar_url)
        embed.add_field(name="***summon**", value="現在自分が接続しているVCにbotを接続させます。\n[TTS]の役職がついている人の文章を読み上げます。",inline=False)
        embed.add_field(name="***disconnect**", value="Botをボイスチャンネルから切断します。",inline=False)

        await ctx.channel.send(embed=embed)  


# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(ChangeHelp(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。