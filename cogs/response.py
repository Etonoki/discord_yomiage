from discord.ext import commands # Bot Commands Frameworkのインポート
import random
import discord

# コグとして用いるクラスを定義。
class Response(commands.Cog):

    # Responseクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    #message...他のctx+argみたいな感じ
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        #メンションを送られた時
        #if self.bot.user in message.mentions:

        # ---------------------------------------------ネタ----------------------------------------------------#

        if message.content == "ここすき":
            await message.channel.send("ワイトもそう思います。")

        if "敗北者" in message.content:
            await message.channel.send("ハァ...ハァ...敗北者...?")
            await message.channel.send("取り消せよ...!!今の言葉...!!")

        if message.content.startswith('ジャンケン@') or message.content.startswith('ジャンケン＠'):
            your_hand = message.content[9:]
            m = random.randint(1, 99)
            msg = ""
            if m == 1:
                if your_hand == "グー":
                    msg += "じゃんけんポン！:v:\n"
                if your_hand == "チョキ":
                    msg += "じゃんけんポン！:hand_splayed:\n"
                if your_hand == "パー":
                    msg += "じゃんけんポン！:fist:\n"
                msg += ":regional_indicator_y::regional_indicator_o::regional_indicator_u: " \
                    ":regional_indicator_w::regional_indicator_i::regional_indicator_n:\nやるやん！:confused: " \
                    "\n明日は俺にリベンジさせて。\nでは、どうぞ。"
            else:
                if your_hand == "グー":
                    msg += "じゃんけんポン！:hand_splayed:\n"
                if your_hand == "チョキ":
                    msg += "じゃんけんポン！:fist:\n"
                if your_hand == "パー":
                    msg += "じゃんけんポン！:v:\n"
                msg += ":regional_indicator_y::regional_indicator_o::regional_indicator_u: " \
                    ":regional_indicator_l::regional_indicator_o::regional_indicator_s::regional_indicator_e:\n" \
                    "俺の勝ち！:grin:\n"
                n = random.randint(1, 3)
                if n == 1:
                    msg += "なんで負けたか明日まで考えといてください\nそしたら何かが見えてくるはずです\nほな いただきます:yum:\n\n一日一回勝負\nじゃあ、また明日:raised_hand:"
                if n == 2:
                    msg += "たかがじゃんけん、そう思ってないですか？\nそれやったら明日も俺が勝ちますよ。\nほな いただきます:yum:\n\n一日一回勝負\nじゃあ、また明日:raised_hand:"
                if n == 3:
                    msg += "負けは次に繋がるチャンスです。\nネバーギブアップ！\nほな いただきます:yum:\n\n一日一回勝負\nじゃあ、また明日:raised_hand:"
            await message.channel.send(msg)

        if "ぬるぽ" in message.content:
            #msg = ""
            #for aaa in range(message.content.count("ぬるぽ")):
            #    msg += "ｶﾞ"
            #msg += "ｯ"
            await message.channel.send("ｶﾞｯヽ(# ﾟДﾟ)ﾉ┌┛∑(ﾉ´д`)ﾉ")

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(Response(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。