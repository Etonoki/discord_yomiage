from discord.ext import commands
import discord

# コグとして用いるクラスを定義。
class ManageRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #特定のメッセージにリアクションがついたときの動作
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        if payload.message_id == 667352897654095893:
            guild = self.bot.get_guild(payload.guild_id) 
            member = guild.get_member(payload.user_id)
            #絵文字によって判定
            if payload.emoji.name == '\U0001F7E6':#blue
                setrole = guild.get_role(638385207254450194)
                await member.add_roles(setrole)
            if payload.emoji.name == '\U0001F7E5':#red
                setrole = guild.get_role(638385201214521360)
                await member.add_roles(setrole)
            if payload.emoji.name == '\U0001F7E8':#yellow
                setrole = guild.get_role(639500455248003075)
                await member.add_roles(setrole)
            if payload.emoji.name == '\U0001F7EA':#purple
                setrole = guild.get_role(639500452588814346)
                await member.add_roles(setrole)
            if payload.emoji.name == '\U0001F7E7':#orange
                setrole = guild.get_role(639500546935357441)
                await member.add_roles(setrole)
            if payload.emoji.name == '\U0001F7E9':#green
                setrole = guild.get_role(639500153979535402)
                await member.add_roles(setrole)
            
            #メンバー
            role1 = guild.get_role(639504047480635422)
            #TTS
            role2 = guild.get_role(640096773087428610)
            await member.add_roles(role1)
            await member.add_roles(role2)

    #特定のメッセージでリアクションが外れた時の動作
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
        if payload.message_id == 667352897654095893:
            guild = self.bot.get_guild(payload.guild_id) 
            member = guild.get_member(payload.user_id)
            #絵文字によって判定
            if payload.emoji.name == '\U0001F7E6':#blue
                setrole = guild.get_role(638385207254450194)
                await member.remove_roles(setrole)
            if payload.emoji.name == '\U0001F7E5':#red
                setrole = guild.get_role(638385201214521360)
                await member.remove_roles(setrole)
            if payload.emoji.name == '\U0001F7E8':#yellow
                setrole = guild.get_role(639500455248003075)
                await member.remove_roles(setrole)
            if payload.emoji.name == '\U0001F7EA':#purple
                setrole = guild.get_role(639500452588814346)
                await member.remove_roles(setrole)
            if payload.emoji.name == '\U0001F7E7':#orange
                setrole = guild.get_role(639500546935357441)
                await member.remove_roles(setrole)
            if payload.emoji.name == '\U0001F7E9':#green
                setrole = guild.get_role(639500153979535402)
                await member.remove_roles(setrole)
            
            
            #await channel.send("<@{}> さん、いらっしゃいませ！\nよければ{} をご記入ください！\nテンプレどうぞ( ´･ω･)⊃旦".format(payload.user_id,mentionchannel.mention)) 
            #await channel.send("【名前】\n【性別】\n【年齢】\n【趣味】\n【一言】") 
            
            #デフォルトの絵文字は判定が困難なので自前で用意した絵文字のIDで判別
            #if(payload.emoji.id == 638406982289588245):
            #    await member.add_roles(arole)

    


# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(ManageRole(bot)) # ResponseにBotを渡してインスタンス化し、Botにコグとして登録する。