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

    @commands.command()
    async def vc(self, ctx):
        if ctx.channel.category.id == 660068529873354752:
            category = self.bot.get_channel(660068529873354752)
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

    #チャット全削除、全消し要らんわってなった
    #@commands.command()
    #@commands.has_permissions(manage_messages=True)
    #async def delete(self, ctx):
    #    await ctx.channel.purge(limit=None)        


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

    ###添付全部保存
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return

        if len(message.attachments) == 0:
            return

        sendlist = []
        channel = self.bot.get_channel(695975015451197460)
        
        for atc in message.attachments:
            #画像データを格納（保存しない）
            image = io.BytesIO(await atc.read())
            #image = io.BytesIO(await atc.read(use_cached=True))
            sendlist.append(discord.File(image,atc.filename))

        ##送信
        await channel.send(files=sendlist)

    ###削除保存
    @commands.Cog.listener()
    async def on_raw_message_delete(self,payload):
        channel = self.bot.get_channel(670501060841963540)
        embed = discord.Embed(title='削除',description=payload.cached_message.content,color=0xff40ff)
        #embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_author(name=payload.cached_message.author.name,icon_url=payload.cached_message.author.avatar_url)

#        #添付がある場合全て添付
#        sendlist = []
        if len(payload.cached_message.attachments) > 0:
#            for atc in payload.cached_message.attachments:
#                await atc.save(atc.filename)
#                sendlist.append(discord.File(atc.filename))
#            await channel.send(embed=embed,files=sendlist)
            pass
        else:
            await channel.send(embed=embed)

    @commands.command(aliases=['sha'])
    async def share(self, ctx):
        if ctx.author.voice:
            await ctx.send("https://discordapp.com/channels/{}/{}/".format(ctx.guild.id,ctx.author.voice.channel.id))
        else :
            await ctx.send("{} ボイスチャンネルに参加した上で、もう一度実行してください。".format(ctx.author.mention))


# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(ManageChannel(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。