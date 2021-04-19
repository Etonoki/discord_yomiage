from discord.ext import commands # Bot Commands Frameworkをインポート
import discord
import asyncio

# 読み込むコグの名前を格納しておく。
INITIAL_EXTENSIONS = [
    'cogs.response',
    'cogs.changehelp',
    #'cogs.speaker',
    'cogs.managerole',
    'cogs.restart',
    'cogs.dark',
    'cogs.nolog',
    #'cogs.talk',
    'cogs.weather',
    'cogs.managechannel'
]

# クラスの定義。ClientのサブクラスであるBotクラスを継承。
class Zattu(commands.Bot):

    # Zattanのコンストラクタ。
    def __init__(self, command_prefix):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(command_prefix)

        # INITIAL_COGSに格納されている名前から、コグを読み込む。
        # エラーが発生した場合は、エラー内容を表示。
        for cog in INITIAL_EXTENSIONS:
            self.load_extension(cog)

    # Botの準備完了時に呼び出されるイベント
    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')

# Zattanのインスタンス化及び起動処理。らぁら
if __name__ == '__main__':
    zattu = Zattu(command_prefix='/')
    zattu.run('NjM5NDk1NzEyNjM1MDkzMDE1.XbsG7w.rn-dZI4bex9YqdXDt_cqKHf18L8')