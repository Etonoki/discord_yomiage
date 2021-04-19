from discord.ext import commands # Bot Commands Frameworkのインポート
import random
import discord
import asyncio
import io
import aiohttp


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
    async def goat(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://placegoat.com/400") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'goat.jpg'))
        

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



    #message...他のctx+argみたいな感じ
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        #メンションを送られた時
        #if self.bot.user in message.mentions:

        if "ぴえん" in message.content:
            await message.add_reaction(chr(0x1F97A))

        if message.content.startswith("."):
            await asyncio.sleep(3)
            await message.delete()


# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(Response(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。