from discord.ext import commands # Bot Commands Frameworkをインポート
import discord
import asyncio
import os

token = os.environ['DISCORD_BOT_TOKEN']

# 読み込むコグの名前を格納しておく。
INITIAL_EXTENSIONS = [
    'cogs.bump',
    'cogs.gatya',
    'cogs.response',
    'cogs.talk2',
    'userlist',
    #'cogs.changehelp', こんなコマンド打つやつ見たことない
    'cogs.speaker',
    'cogs.managechannel'
]

# クラスの定義。ClientのサブクラスであるBotクラスを継承。
class Zattan(commands.Bot):

    # Zattanのコンストラクタ。
    def __init__(self, command_prefix, intents):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(command_prefix, intents=intents)

        # INITIAL_COGSに格納されている名前から、コグを読み込む。
        # エラーが発生した場合は、エラー内容を表示。
        for cog in INITIAL_EXTENSIONS:
            self.load_extension(cog)

    # Botの準備完了時に呼び出されるイベント
    async def on_ready(self):
        #こっから音声処理
        #if not discord.opus.is_loaded():
        #    discord.opus.load_opus("heroku-buildpack-libopus")
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')

# Zattanのインスタンス化及び起動処理
if __name__ == '__main__':
    discord_intents = discord.Intents.all()
    zattan = Zattan(command_prefix='*',intents=discord_intents)
    zattan.run(token)
