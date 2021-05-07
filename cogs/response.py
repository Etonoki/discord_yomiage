from discord.ext import commands # Bot Commands Frameworkのインポート
import random
import discord
import asyncio
import io
import aiohttp

#鯖
piriko = 824660451509796914
#通話募集チャンエル
tuuwa = 840085935860613151

# コグとして用いるクラスを定義。
class Response(commands.Cog):

    # Responseクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def dog(self, ctx):
        url = ""
        async with aiohttp.ClientSession() as session:
            async with session.get('https://dog.ceo/api/breeds/image/random') as r:
                if r.status == 200:
                    js = await r.json()
                    url = js['message']

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'dog.jpg'))
    
    @commands.command()
    async def cat(self, ctx):
        url = ""
        async with aiohttp.ClientSession() as session:
            async with session.get('http://aws.random.cat/meow') as r:
                if r.status == 200:
                    js = await r.json()
                    url = js['file']

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'cat.jpg'))

    @commands.command()
    async def fox(self, ctx):
        url = ""
        async with aiohttp.ClientSession() as session:
            async with session.get('https://randomfox.ca/floof/') as r:
                if r.status == 200:
                    js = await r.json()
                    url = js['image']

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'fox.jpg'))

    @commands.command()
    async def shiba(self, ctx):
        url = ""
        async with aiohttp.ClientSession() as session:
            async with session.get('http://shibe.online/api/shibes') as r:
                if r.status == 200:
                    js = await r.json()
                    url = js[0]

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'shiba.jpg'))

#####################################################################################################################

    """
    ###入ったときにメンション
    @commands.Cog.listener()
    async def on_member_join(self,member):
        if member.bot:
            return
        
        guild = self.bot.get_guild(piriko)
        channel = guild.get_channel(tuuwa)
        
        await asyncio.sleep(90)
        
        #botがボイスチャットにいる且つ通話に参加していない場合
        if guild.voice_client.is_connected() and member.voice is None:
            await channel.send('{} さん いらっしゃいませ！\nよければ通話にご参加くださいね。'.format(member.mention))
    """

    #message...他のctx+argみたいな感じ
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        guild = self.bot.get_guild(piriko)
        channel = guild.get_channel(tuuwa)
        
        #メンションを送られた時
        #if self.bot.user in message.mentions:

        if "ぴえん" in message.content:
            await message.add_reaction(chr(0x1F97A))

        if message.content.startswith("."):
            await asyncio.sleep(3)
            await message.delete()
        
        if message.channel.id == 824660592534093875:
            await asyncio.sleep(90)
            #botがボイスチャットにいる且つ通話に参加していない場合
            if guild.voice_client.is_connected() and member.voice is None:
                await channel.send('{} さん いらっしゃいませ！\nよければ通話にご参加くださいね。'.format(member.mention))
            
            
# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(Response(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。
