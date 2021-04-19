from discord.ext import commands
import discord

# コグとして用いるクラスを定義。
class ManageRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #役職変更
    #イベントハンドラ使うときはclientがself.botでいいぽい。discord.ext.commands.bot以下
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = self.bot.get_channel(payload.channel_id) 
        if channel.id == 638152773338136599:
            guild = self.bot.get_guild(payload.guild_id) 
            member = guild.get_member(payload.user_id)

            #メンバー
            role1 = guild.get_role(639504047480635422)
            #channel = self.bot.get_channel(638152970567155712)
            #mentionchannel = self.bot.get_channel(638739366964887553)

            #TTS
            role2 = guild.get_role(640096773087428610)
        
            await member.add_roles(role1)
            await member.add_roles(role2)

            #await channel.send("<@{}> さん、いらっしゃいませ！\nよければ{} をご記入ください！\nテンプレどうぞ( ´･ω･)⊃旦".format(payload.user_id,mentionchannel.mention)) 
            #await channel.send("【名前】\n【性別】\n【年齢】\n【趣味】\n【一言】") 
            
            #デフォルトの絵文字は判定が困難なので自前で用意した絵文字のIDで判別
            #if(payload.emoji.id == 638406982289588245):
            #    await member.add_roles(arole)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(ManageRole(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。