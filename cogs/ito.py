import discord
from discord.ext import commands
import random

life = 0
senddict = {}
resultdict = {}
availablehint = 0
ramcopy = 0
count = 0
themalist = [
    "モテる条件・特技",
    "強そうな効果音(創作可)",
    "テンションの上がるもの・こと",
    "地球観光に来た宇宙人にあげたいお土産",
    "なりたい生き物",
    "欲しい(手に入れたい)\n特殊能力・武器(必殺技・道具)",
    "生き物の強さ",
    "酒のつまみ・居酒屋メニューの人気",
    "一人暮らしに必用なもの",
    "グッとくる仕草・行動",
    "小学生が好きな言葉",
    "時代遅れの言葉",
    "職業の人気",
    "歴史上人物の人気",
    "有名人の人気",
    "こわいもの",
    "うれしいこと",
    "強そうな言葉",
    "カッコいい苗字、名前",
    "趣味の人気",
    "駅の人気",
    "飲み物の人気",
    "アニメ・漫画の人気",
    "映画の人気",
    "ミュージシャンの人気",
    "飲み物の人気",
    "有名人の人気(芸能人・芸人・選手など)", 
    "スポーツの人気",
    "テレビバングみの人気(ドラマ含む)",
    "やわらかそうなもの",
    "重そうなもの",
    "ゾンビと戦うときに持っていいたいもの",
    "飲み物の人気",
    "無人島に持っていきたいもの",
    "デートスポットの人気",
    "グッとくる仕草・行動",
    "されたいプロポーズ(セリフ・シチュエーション)",
    "時代遅れの言葉",
    "オタクが選ぶセリフ・設定"
]

class Ito(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    #rule

    #ヒントの実装、上から出した数字より大きいか小さいか使える。1回だけ
    @commands.command()
    async def hint(self, ctx):
        global senddict
        global availablehint
        #ユーザーに送った要素がある=ゲームが開始していれば実行
        if len(senddict) > 0:
            if availablehint > 0:
                availablehint = availablehint - 1
                ccc = random.randint(1, 100)
                await ctx.send("ヒント：" + ccc)
            else :
                await ctx.send("ヒントはもう使えないよ！")

    #arg1 各個人に配られる数の数
    @commands.command()
    async def ito(self, ctx, arg1:int):
        global senddict
        global availablehint
        global ramcopy
        global life
        #通話に参加しているメンバーリスト
        memlist = []
        #メンバーの数だけ作成した数のリスト
        ramnumber = []
        #メンバーに配った内容を格納する辞書
        senddict = {}
        #ライフ
        life = 3
        #ヒント残数
        availablehint = 1

        count = 0

        if arg1 > 5 and 0 >= arg1:
            ctx.send("配布数は5以下で指定してください")
            return

        #お題出力
        ccc = random.randint(1, len(themalist)-1)
        aaa = themalist[ccc]
        bbb = themalist[ccc + 1]
        await ctx.send(aaa + " or " + bbb)

        #bot以外のユーザーの情報を取得と人数のカウント
        for member in ctx.author.voice.channel.members:
            if member.bot == False:
                memlist.append(member)
                count = count + 1

        #人数*数字の個数だけループ処理、ランダムな数を取り出してramnumberに格納
        while len(ramnumber) < count * arg1:
            n = random.randint(1, 100)
            if not n in ramnumber:
                ramnumber.append(n)

        ramcopy = sorted(ramnumber)
        
        #ramnumberを各ユーザーに配布
        for aaa in memlist:
            user = ctx.guild.get_member(aaa.id)
            pop = "あなたの数字は："
            for i in range(arg1):
                bbb = ramnumber.pop()
                pop = pop + str(bbb) + ","
                #各ユーザーに配った数とidを格納
                senddict[bbb] = user.id
            await user.send(pop)

        #ユーザーに送った情報をキーで小さい順にソート
        ttt = senddict
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        global senddict
        global resultdict
        global count
        global availablehint
        global life
        global ramcopy


        #ユーザーに送った要素がある=ゲームが開始していれば実行
        if len(senddict) > 0:
            #数字がリストにある
            if int(message.content) in senddict:
                #数字と所持者が正しい
                if message.author.id == senddict[int(message.content)]:
                    #最小の数字かどうか
                    if ramcopy[0] == int(message.content):
                        #0番目取り出し、数字がk,送信者idがvに格納
                        resultdict[count] = [message.author.name,message.content]
                        
                        del ramcopy[0]
                        del senddict[int(message.content)]
                    else :
                        life = life - 1
                        await message.channel.send("少ない数字を持っている人がいるよ！：残りライフ{}".format(life))
                        return
                else :
                    return
            else :
                return
        else :
            return
        
        embed=discord.Embed(title="**結果**", color=0xff40ff)
        for k ,v in resultdict.items():
            embed.add_field(name="{}:".format(v[0]),value=v[1],inline=False)
        embed.add_field(name="\n残りヒント",value="{}".format(availablehint),inline=False)
        embed.add_field(name="残りライフ",value="{}".format(life),inline=True)
        await message.channel.send(embed=embed)

#凡そ完成したらここを使えるようにする
    @ito.error
    async def ito_error(self, ctx, error):
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。\n例：``/ito 5``\n各ユーザーに数字5つでゲームを始めます。')

def setup(bot):
    bot.add_cog(Ito(bot))
