from discord.ext import commands
import discord
from discord import embeds

# コグとして用いるクラスを定義。
class ChangeHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    #helpコマンド修正。埋め込みメッセージ
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="汎用Bot機能一覧", color=0xff40ff)
        embed.set_author(name=self.bot.user.name,icon_url=self.bot.user.avatar_url)
        embed.add_field(name="**話題**", value="\"話題\"という入力に反応して話題を提供します",inline=False)
        #embed.add_field(name="**雑談機能**", value="Botにメンションを送ることで当たり障りのない返信が来ます。",inline=False)
        embed.add_field(name="**/thelp**", value="TTS(読み上げ機能)に関するヘルプを表示します。",inline=False)
        embed.add_field(name="**/mhelp**", value="音楽Botのヘルプを表示します。",inline=False)
        embed.add_field(name="**/share**", value="ボイスチャンネルの画面共有URLを出力します。",inline=False)
        embed.add_field(name="**/weather X**", value="Xの天気を返信。以下のcity titleのみ対応\n http://weather.livedoor.com/forecast/rss/primary_area.xml", inline=False)
        embed.add_field(name="**/vc**", value="ゲームカテゴリでボイスチャンネルを作成/します。", inline=False)
        embed.add_field(name="**.〇〇**", value=".で始まるメッセージを3秒後に削除します。証拠隠滅に", inline=False)

        await ctx.channel.send(embed=embed)

    @commands.command()
    async def thelp(self, ctx):
        embed=discord.Embed(title="TTS機能一覧", color=0xff40ff)
        embed.set_author(name=self.bot.user.name,icon_url=self.bot.user.avatar_url)
        embed.add_field(name="**/summon**", value="現在自分が接続しているVCにbotを接続させます。\n[TTS]の役職がついている人の文章を読み上げます。",inline=False)
        embed.add_field(name="**/disconnect**", value="Botをボイスチャンネルから切断します。",inline=False)
        embed.add_field(name="**/speaker X**", value="話者。\n1:show(男性)\n2:haruka(女性)\n3:hikari(女性)\n4:takeru(男性)\n5:santa(サンタ)\n6:bear(凶暴なクマ)\n初期値3",inline=False)
        embed.add_field(name="**/pitch Y**", value="音の高低を数値で指定します。値が小さいほど低い音になります。\n初期値110:範囲50~200(%)",inline=False)
        embed.add_field(name="**/speed Z**", value="話す速度を数値で指定します。値が小さいほど遅い話し方になります。\n初期値110:範囲50~400(%)",inline=False)
        embed.add_field(name="**/config X Y Z**", value="上記を一度に設定できます。3つ同時に指定してください。",inline=False)
        embed.add_field(name="**/emotion X Y**", value="第一引数に感情、第二引数に感情レベル(1~4)を指定します。\n1:happiness(喜)\n2:anger(怒)\n3:sadness(悲)\n4:default(初期値)",inline=False)

        await ctx.channel.send(embed=embed)  

    @commands.command()
    async def mhelp(self, ctx):
        guild = self.bot.get_guild(638152773338136597)
        user1 = guild.get_member(620157803511808000)
        
        embed=discord.Embed(title="音楽Bot機能一覧", color=0xff40ff)
        embed.set_author(name=user1.name,icon_url=user1.avatar_url)
        embed.add_field(name="**!summon**", value="現在自分が接続しているVCにbotを接続させます",inline=False)
        embed.add_field(name="**!play <URL/検索ワード>**", value="指定したURL・検索ワードで再生します",inline=False)
        embed.add_field(name="**!np**", value="現在再生中の音楽を表示します",inline=False)
        embed.add_field(name="**!pause**", value="再生を一時停止します",inline=False)
        embed.add_field(name="**!resume**", value="一時停止を解除します",inline=False)
        embed.add_field(name="**!skip**", value="現在再生中の音楽をスキップします",inline=False)
        embed.add_field(name="**!queue**", value="現在再生リスト（キュー）に入っている曲を一覧表示します",inline=False)
        embed.add_field(name="**!clear**", value="現在再生リスト（キュー）に入っている曲を消去します",inline=False)
        embed.add_field(name="**!volume [0-100]**", value="ボリュームを0から100%で指定します\n初期値10",inline=False)
        embed.add_field(name="**!stream <URL>**", value="YouTube LiveやTwitchの配信をリアルタイムに再生します",inline=False)
        embed.add_field(name="**!disconnect**", value="botをVCから切断させます",inline=False)
        embed.add_field(name="**!restart**", value="botを再起動させます",inline=False)
        embed.add_field(name="**!shutdown**", value="botを停止させます。\nサーバーの機能で無理矢理立ち上げ直す形なので、``!restart``で対応できない場合のみ行ってください。",inline=False)

        await ctx.channel.send(embed=embed)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(ChangeHelp(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。