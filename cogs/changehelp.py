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
        embed.add_field(name="***help**", value="TTS(読み上げ機能)に関するヘルプを表示します。",inline=False)
        embed.add_field(name="**/mhelp**", value="音楽Botのヘルプを表示します。",inline=False)
        embed.add_field(name="**/share**", value="ボイスチャンネルの画面共有URLを出力します。",inline=False)
        #embed.add_field(name="**/weather X**", value="Xの天気を返信。以下のcity titleのみ対応\n http://weather.livedoor.com/forecast/rss/primary_area.xml", inline=False)
        embed.add_field(name="**/vc**", value="ゲームカテゴリでボイスチャンネルを作成/削除します。", inline=False)
        embed.add_field(name="**/delete X**", value="Xだけログを遡って自身の発言を削除します。``/delete``のみなら50ほど、``/del 0``でチャンネルのログ全て消します。", inline=False)
        embed.add_field(name="**/nolog X**", value="botが再起動するまで、実行したチャンネルでの発言をX秒後に削除します。初期値10", inline=False)
        embed.add_field(name="***tts**", value="TTSの権限を付与/はく奪します。", inline=False)
        embed.add_field(name="**.〇〇**", value=".で始まるメッセージを3秒後に削除します。証拠隠滅に", inline=False)

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