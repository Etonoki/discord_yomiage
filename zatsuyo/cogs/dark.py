import discord
from discord.ext import commands

#ban実行可能ユーザー
bskerlist = {
    249176611553935363:"えと",
    645141235056771082:"ぴりこ",
    646520557583466560:"ぶすじま"
}

#ロール判定用
def check_bsk(ctx):
    if ctx.message.author.id in bskerlist.keys():
        return True

class Dark(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        #DM送られたときの処理
        if not message.guild:
            #匿名チャンネル
            channel1 = self.bot.get_channel(662448789910585370)
            #送信先匿名（笑）チャンネル
            channel2 = self.bot.get_channel(664095767778033674)

            embed = discord.Embed(
                description=message.content,
                color=0xff40ff
            )
            
            #embed.set_thumbnail(url=self.bot.user.avatar_url)

            embed.set_author(
                name=message.author.name,
                icon_url=message.author.avatar_url
            )
            
            await channel1.send(message.content)
            await channel2.send(embed=embed)


    @commands.check(check_bsk)
    @commands.dm_only()
    @commands.command()
    async def ban(self,ctx,arg):
        guild = self.bot.get_guild(638152773338136597)
        user = guild.get_member(int(arg))
        await ctx.send("{}をbanしました".format(user.name))
        await user.ban()

    #ぶすじま用、ランダムにメッセージ送る迷惑なやつ
    @commands.command()
    async def rmsg(self, ctx):
        #なんさばuserlistの中のbot以外を出力
        li = [member for member in self.bot.get_all_members() if member.bot == False and member.guild.id == 638152773338136597 and member.status == discord.Status.online and member.id != ctx.author.id]
        #print(li)
        target = li[random.randint(1,len(li))]
        await ctx.send("{} {} が通話をしたいようです。\nなお、本通知はBotがランダムに選んだ人に対して送っています。".format(target.mention,ctx.author.name))
        #print(random.choice(li))


def setup(bot):
    bot.add_cog(Dark(bot))
