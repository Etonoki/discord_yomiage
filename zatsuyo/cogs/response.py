from discord.ext import commands # Bot Commands Frameworkのインポート
import random
import discord
import asyncio
import io
import aiohttp

wadai = ["季節","ニュース","健康","旅","仕事","ファッション","好きなお酒","出身地","最近見た動画","ペット","学生時代","テレビやラジオ番組","誕生日","血液型","好きな食べ物","最近食べたおいしいもの","ハマっている遊び","趣味"]


jimlist = [
    "腹筋 6LDK かい！",
    "二頭がいいね！チョモランマ！",
    "大胸筋が歩いてる！",
    "筋肉本舗！はいズドーン！",
    "泣く子も黙る大腿筋！",
    "肩にちっちゃい重機のせてんのかい！",
    "背中に鬼神が宿ってる！",
    "頑張るあなたは美しい！",
    "腹筋板チョコ！バレンタイン！",
    "これが二頭の新時代…！",
    "はち切れそうな大胸筋！",
    "出たな！プロポーションおばけ！",
    "ザッツアグレート大腿筋！",
    "とれたて新鮮肩メロン！",
    "背中に世界を背負ってる！",
    "仕上がってるよ！仕上がってるよ！\n頑張るあなたは美しい！"
]


# コグとして用いるクラスを定義。
class Response(commands.Cog):

    # Responseクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ron(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://cdn.discordapp.com/attachments/644791792406888480/664418287110586407/tenor.gif") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ron.gif'))
    
    @commands.command()
    async def busujima(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://cdn.discordapp.com/attachments/644791792406888480/664420507680112640/tenor_1.gif") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'busujima.gif'))

    @commands.command()
    async def piriko(self, ctx):
        async with aiohttp.ClientSession() as session:
            gifs = [
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/644791792406888480/664420519063584768/391x220xb5e9b4f86ce43ca65bd79c89.gif",
                "https://cdn.discordapp.com/attachments/640535455766413342/665452004138549252/tenor_1.gif"
            ]
            async with session.get(random.choice(gifs)) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'piriko.gif'))

    
    @commands.command()
    async def anima(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://cdn.discordapp.com/attachments/644791792406888480/665543078177669123/tenor_2.gif") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'anima.gif'))

                
    @commands.command()
    async def tom(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://cdn.discordapp.com/attachments/650352484560404480/665523061159755796/i.imgur.com_PgZuY09.gif") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'anima.gif'))


    @commands.command()
    async def kill(self, ctx, arg):
        await ctx.send("{} を処分しました。".format(arg))


    #message...他のctx+argみたいな感じ
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        #メンションを送られた時
        #if self.bot.user in message.mentions:

        # ---------------------------------------------ネタ----------------------------------------------------#

        if "話題" == message.content:
            www = random.choice(wadai)
            await message.channel.send("「{}」の話なんてどうでしょう？".format(www))

        if message.content.startswith("ジム"):
            if message.author.id == 640845525691793409:
                await message.channel.send(random.choice(jimlist))

        if "敗北者" in message.content:
            async with aiohttp.ClientSession() as session:
                haiboku = [
                    "https://cdn.discordapp.com/attachments/659742326502981662/666190164464238603/images.jpg",
                    "https://cdn.discordapp.com/attachments/650352484560404480/666190128997335090/haiboku.png"
                ]
                n = random.randint(1, 99)
                if n < 10:
                    choice = haiboku[1]
                else:
                    choice = haiboku[0]
                async with session.get(choice) as resp:
                    if resp.status != 200:
                        return await message.channel.send('Could not download file...')
                    data = io.BytesIO(await resp.read())
                    await message.channel.send(file=discord.File(data, 'haibokusya.gif'))

        if message.content.startswith("."):
            await asyncio.sleep(3)
            await message.delete()

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(Response(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。