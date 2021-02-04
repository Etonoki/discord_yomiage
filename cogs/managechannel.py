from discord.ext import commands
import discord
import os
import datetime
from discord import embeds
import asyncio

ID_CATEGORY = 660068529873354752 #ゲームカテゴリID


class ManageChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vc(self, ctx):
        if ctx.channel.category.id == ID_CATEGORY:
            category = self.bot.get_channel(ID_CATEGORY)
            name = ctx.channel.name
            check = self.bot.get_all_channels()
            
            #テキストチャンネルと同一の名前のチャンネルを全て取得
            chan = [channel for channel in check if channel.name == name]
            #取得したチャンネル数が1、つまりテキストチャンネルのみの場合は作成、1より多い場合は全て削除
            if len(chan) > 1:
                #取得したチャンネルの中から、ループ、VoiceChannelのみを適用
                for aaa in chan:
                    if isinstance(aaa,discord.channel.VoiceChannel):
                        await aaa.delete()
                bbb = await ctx.send("{} ボイスチャンネルを削除しました".format(ctx.author.mention))
                await asyncio.sleep(10)
                await bbb.delete()
            else:
                #vcがない場合の処理
                payload = {'name': name, 'category': category, 'position': 0}
                channel = await ctx.guild.create_voice_channel(**payload)
                bbb = await ctx.send("{} ボイスチャンネルを作成しました".format(ctx.author.mention))
                await asyncio.sleep(10)
                await bbb.delete()

    #チャット全削除
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx):
        await ctx.channel.purge()

    #チャット全削除
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def kanri(self, ctx):
        embed=discord.Embed(title="**管理コマンド一覧**", color=0xff40ff)
        #embed.add_field(name="**/replace**", value="交換スレッドログからスレッドを復活させます\n管理者には必要ありませんが、権限同期がバグり易いのでこちらを推奨")
        embed.add_field(name="**/delete**", value="テキストチャンネルのログを全て削除します\n元に戻せないので注意されたし")
        embed.add_field(name="**/restart**", value="botを再起動させます",inline=False)
        embed.add_field(name="**/speakUser**", value="ユーザーの設定ファイルを出力します。",inline=False)

        await ctx.channel.send(embed=embed)

    @commands.command(aliases=['sha'])
    async def share(self, ctx):
        if ctx.author.voice:
            await ctx.send("https://discordapp.com/channels/{}/{}/".format(ctx.guild.id,ctx.author.voice.channel.id))
        else :
            await ctx.send("{} ボイスチャンネルに参加した上で、もう一度実行してください。".format(ctx.author.mention))
        

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(ManageChannel(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。