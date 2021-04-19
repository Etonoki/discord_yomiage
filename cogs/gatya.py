import discord
from discord.ext import tasks, commands
import json
import asyncio
import aiohttp
import random
import io

branch = "https://starlight.kirara.ca"
gatya_url = "https://starlight.kirara.ca/api/v1/list/card_t"


class Gatya(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.a_list = []
        self.b_list = []
        self.c_list = []

    #初期動作
    @commands.Cog.listener()
    async def on_ready(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(gatya_url) as r:
                if r.status == 200:
                    idle_dict = await r.json()

        for idle in idle_dict["result"]:
            #レアリティごとにリストに格納
            if idle["rarity_dep"]["rarity"] == 7:
                self.a_list.append(idle)
            elif idle["rarity_dep"]["rarity"] == 5:
                self.b_list.append(idle)
            elif idle["rarity_dep"]["rarity"] == 3:
                self.c_list.append(idle)

#    @getdate.before_loop
#    async def before_getdate(self):
#        await self.bot.wait_until_ready()


    #ガチャ
    @commands.group(invoke_without_command=True)
    async def gatya(self, ctx):
        

#        #ガチャ処理
        rdm = random.choices(range(100),k=10)
#        for r in rdm:
#            if r > 96:
#                #ssr封筒gif################################################
#                huto = ""
#            else:
#                huto = ""
#
#        async with aiohttp.ClientSession() as session:
#            async with session.get(huto) as resp:
#                if resp.status != 200:
#                    return await ctx.send('Could not download file...')
#                data = io.BytesIO(await resp.read())
#                await ctx.send(file=discord.File(data, 'huto.gif'))
#        
#        #gif再生
#        await asyncio.sleep(3)

        #ガチャ出力、レアリティの中からランダムにカードを取得
        for i in range(10):
            #ラス1以外、8割
            if rdm[i] < 87 and i != 9:
                out = random.choice(self.c_list)
                #カード情報の取得
                my_url = branch + out["ref"]
                async with aiohttp.ClientSession() as session:
                    async with session.get(my_url) as r:
                        if r.status == 200:
                            card = await r.json()
                            li = card["result"][0]['name']
                            await ctx.send(f"【R】{li}")
                continue

            elif rdm[i] > 96:
                out = random.choice(self.a_list)
                #カード情報の取得
                my_url = branch + out["ref"]
                async with aiohttp.ClientSession() as session:
                    async with session.get(my_url) as r:
                        if r.status == 200:
                            card = await r.json()

                #カード画像の出力
                
                async with aiohttp.ClientSession() as session:
                    async with session.get(card["result"][0]['sign_image_ref']) as resp:
                        if resp.status != 200:
                            return await ctx.send('Could not download file...')
                        data1 = io.BytesIO(await resp.read())

                async with aiohttp.ClientSession() as session:
                    async with session.get(card["result"][0]['spread_image_ref']) as resp:
                        if resp.status != 200:
                            return await ctx.send('Could not download file...')
                        data2 = io.BytesIO(await resp.read())
                        li = card["result"][0]['name']
                        msg = await ctx.send(file=discord.File(data1, f'sign{i}.png'))
                        await ctx.send(f"【SSR】{li}",file=discord.File(data2, f'image{i}.png'))
                        await asyncio.sleep(1)
                        await msg.delete()

            else:
                out = random.choice(self.b_list)
                #カード情報の取得
                my_url = branch + out["ref"]
                async with aiohttp.ClientSession() as session:
                    async with session.get(my_url) as r:
                        if r.status == 200:
                            card = await r.json()

                #カード画像の出力
                async with aiohttp.ClientSession() as session:
                    async with session.get(card["result"][0]['spread_image_ref']) as resp:
                        if resp.status != 200:
                            return await ctx.send('Could not download file...')
                        data = io.BytesIO(await resp.read())
                        li = card["result"][0]['name']
                        await ctx.send(f"【SR】{li}",file=discord.File(data, f'image{i}.png'))





    #ガチャ
    @gatya.command()
    async def fes(self, ctx):
#        #ガチャ処理
        rdm = random.choices(range(100),k=10)
#        for r in rdm:
#            if r > 96:
#                #ssr封筒gif################################################
#                huto = ""
#            else:
#                huto = ""
#
#        async with aiohttp.ClientSession() as session:
#            async with session.get(huto) as resp:
#                if resp.status != 200:
#                    return await ctx.send('Could not download file...')
#                data = io.BytesIO(await resp.read())
#                await ctx.send(file=discord.File(data, 'huto.gif'))
#        
#        #gif再生
#        await asyncio.sleep(3)

        #ガチャ出力、レアリティの中からランダムにカードを取得
        for i in range(10):
            #ラス1以外、8割
            if rdm[i] < 87 and i != 9:
                out = random.choice(self.c_list)
                #カード情報の取得
                my_url = branch + out["ref"]
                async with aiohttp.ClientSession() as session:
                    async with session.get(my_url) as r:
                        if r.status == 200:
                            card = await r.json()
                            li = card["result"][0]['name']
                            await ctx.send(f"【R】{li}")
                continue

            elif rdm[i] > 93:
                out = random.choice(self.a_list)
                #カード情報の取得
                my_url = branch + out["ref"]
                async with aiohttp.ClientSession() as session:
                    async with session.get(my_url) as r:
                        if r.status == 200:
                            card = await r.json()

                #カード画像の出力
                
                async with aiohttp.ClientSession() as session:
                    async with session.get(card["result"][0]['sign_image_ref']) as resp:
                        if resp.status != 200:
                            return await ctx.send('Could not download file...')
                        data1 = io.BytesIO(await resp.read())

                async with aiohttp.ClientSession() as session:
                    async with session.get(card["result"][0]['spread_image_ref']) as resp:
                        if resp.status != 200:
                            return await ctx.send('Could not download file...')
                        data2 = io.BytesIO(await resp.read())
                        li = card["result"][0]['name']
                        msg = await ctx.send(file=discord.File(data1, f'sign{i}.png'))
                        await ctx.send(f"【SSR】{li}",file=discord.File(data2, f'image{i}.png'))
                        await msg.delete()

            else:
                out = random.choice(self.b_list)
                #カード情報の取得
                my_url = branch + out["ref"]
                async with aiohttp.ClientSession() as session:
                    async with session.get(my_url) as r:
                        if r.status == 200:
                            card = await r.json()

                #カード画像の出力
                async with aiohttp.ClientSession() as session:
                    async with session.get(card["result"][0]['spread_image_ref']) as resp:
                        if resp.status != 200:
                            return await ctx.send('Could not download file...')
                        data = io.BytesIO(await resp.read())
                        li = card["result"][0]['name']
                        await ctx.send(f"【SR】{li}",file=discord.File(data, f'image{i}.png'))




    #ガチャ
    @gatya.command()
    async def cheat(self, ctx):
#        #ガチャ処理
        rdm = random.choices(range(100),k=10)
#        for r in rdm:
#            if r > 96:
#                #ssr封筒gif################################################
#                huto = ""
#            else:
#                huto = ""
#
#        async with aiohttp.ClientSession() as session:
#            async with session.get(huto) as resp:
#                if resp.status != 200:
#                    return await ctx.send('Could not download file...')
#                data = io.BytesIO(await resp.read())
#                await ctx.send(file=discord.File(data, 'huto.gif'))
#        
#        #gif再生
#        await asyncio.sleep(3)

        #ガチャ出力、レアリティの中からランダムにカードを取得
        for i in range(10):
            #ラス1以外、8割
            if rdm[i] < 0 and i != 9:
                out = random.choice(self.c_list)
                #カード情報の取得
                my_url = branch + out["ref"]
                async with aiohttp.ClientSession() as session:
                    async with session.get(my_url) as r:
                        if r.status == 200:
                            card = await r.json()
                            li = card["result"][0]['name']
                            await ctx.send(f"【R】{li}")
                continue

            elif rdm[i] > 0:
                out = random.choice(self.a_list)
                #カード情報の取得
                my_url = branch + out["ref"]
                async with aiohttp.ClientSession() as session:
                    async with session.get(my_url) as r:
                        if r.status == 200:
                            card = await r.json()

                #カード画像の出力
                
                async with aiohttp.ClientSession() as session:
                    async with session.get(card["result"][0]['sign_image_ref']) as resp:
                        if resp.status != 200:
                            return await ctx.send('Could not download file...')
                        data1 = io.BytesIO(await resp.read())

                async with aiohttp.ClientSession() as session:
                    async with session.get(card["result"][0]['spread_image_ref']) as resp:
                        if resp.status != 200:
                            return await ctx.send('Could not download file...')
                        data2 = io.BytesIO(await resp.read())
                        li = card["result"][0]['name']
                        msg = await ctx.send(file=discord.File(data1, f'sign{i}.png'))
                        await ctx.send(f"【SSR】{li}",file=discord.File(data2, f'image{i}.png'))
                        await msg.delete()

            else:
                out = random.choice(self.b_list)
                #カード情報の取得
                my_url = branch + out["ref"]
                async with aiohttp.ClientSession() as session:
                    async with session.get(my_url) as r:
                        if r.status == 200:
                            card = await r.json()

                #カード画像の出力
                async with aiohttp.ClientSession() as session:
                    async with session.get(card["result"][0]['spread_image_ref']) as resp:
                        if resp.status != 200:
                            return await ctx.send('Could not download file...')
                        data = io.BytesIO(await resp.read())
                        li = card["result"][0]['name']
                        await ctx.send(f"【SR】{li}",file=discord.File(data, f'image{i}.png'))





#############################################################
#    #ループの作成
#    @tasks.loop(seconds=60.0)
#    async def change_icon(self):
#        guild = self.bot.get_guild(638152773338136597)
#        now = time.now().strftime('%H:%M')
#        if now == '23:59':
#            #アイコン画像取得#######################################################ランダムtyois
#            icons = 
#
#            #アイコン変更
#            async with aiohttp.ClientSession() as session:
#                async with session.get(icons) as resp:
#                    if resp.status != 200:
#                        return
#                    data = io.BytesIO(await resp.read())
#                    await guild.edit(icon=discord.File(data, 'icon.png'))
#            
    


def setup(bot):
    bot.add_cog(Gatya(bot))
