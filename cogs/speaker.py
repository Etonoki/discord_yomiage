import discord
from discord.ext import tasks, commands
import json
import requests
import os
import asyncio

VERSION = "v1"
URL = "https://api.voicetext.jp/%s/tts" % VERSION
key = "sge9n65nsy41mkve"

tenorimori = 753983400859402251
piriko = 824660451509796914

default = {
    "text": "",
    "speaker": "hikari",
    "pitch": 110,
    "speed": 110,
    "volume": 120
}

json_open = open('speakUser.json', 'r', encoding="utf-8_sig")
json_load = json.load(json_open)
dic = json_load

holdlist = []
count = 1

class Speaker(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.mplayer.start()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def restart(self, ctx):
        await self.bot.logout()

        
    ###ttsを付与
    @commands.Cog.listener()
    async def on_member_join(self,member):
        if member.bot:
            return

        guild = member.guild
        ttsrole = guild.get_role(827887373106544682)
        await member.add_roles(ttsrole)

    #特定のメッセージにリアクションがついたときの動作
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        global dic
        guild = self.bot.get_guild(payload.guild_id) 
        member = guild.get_member(payload.user_id)
        userID = str(payload.user_id)
        
        #キーが存在しない場合は追加
        if userID not in dic:
            dic[userID] = default.copy()

        #リアクション絵文字によって判定、数字は組み合わせで作られてるのでunicodeじゃダメ

        #TTS判定
        if payload.message_id == 827892914839355443:
            if payload.emoji.name == '1️⃣':#1
                ttsrole = guild.get_role(827887373106544682)
                await member.add_roles(ttsrole)
                await member.send("TTSを付与しました")
                return
            elif payload.emoji.name == '2️⃣':#2
                if member.voice is None:
                    await member.send('ボイスチャンネルに参加した上で、もう一度実行してください。')
                    return
                else:
                    vc = member.voice.channel
                    await vc.connect()
                    return
            else:
                return


        #話者
        elif payload.message_id == 827892982384164894:
            if payload.emoji.name == '1️⃣':#1
                dic[userID]["speaker"] = "show"
                #showくんならエモート削除
                try:
                    del dic[userID]["emotion"]
                    del dic[userID]["emotion_level"]
                except KeyError as e:
                    pass
            elif payload.emoji.name == '2️⃣':#2
                dic[userID]["speaker"] = "haruka"
            elif payload.emoji.name == '3️⃣':#3
                dic[userID]["speaker"] = "hikari"
            elif payload.emoji.name == '4️⃣':#4
                dic[userID]["speaker"] = "takeru"
            elif payload.emoji.name == '5️⃣':#5
                dic[userID]["speaker"] = "santa"
            elif payload.emoji.name == '6️⃣':#6
                dic[userID]["speaker"] = "bear"
            else:
                return

        #ピッチ
        elif payload.message_id == 827893062876921856:
            if payload.emoji.name == '1️⃣':#1
                dic[userID]["pitch"] = 50
            elif payload.emoji.name == '2️⃣':#2
                dic[userID]["pitch"] = 100
            elif payload.emoji.name == '3️⃣':#3
                dic[userID]["pitch"] = 150
            elif payload.emoji.name == '4️⃣':#4
                dic[userID]["pitch"] = 200
            elif payload.emoji.name == '⬆️':#上
                if dic[userID]["pitch"] <= 190:#200以上ダメ
                    dic[userID]["pitch"] = dic[userID]["pitch"] + 10            
            elif payload.emoji.name == '⬇️':#下
                if dic[userID]["pitch"] >= 10:#0以下ダメ
                    dic[userID]["pitch"] = dic[userID]["pitch"] - 10
            else:
                return

        #スピード
        elif payload.message_id == 827893124244308008:
            if payload.emoji.name == '1️⃣':#1
                dic[userID]["speed"] = 50
            elif payload.emoji.name == '2️⃣':#2
                dic[userID]["speed"] = 100
            elif payload.emoji.name == '3️⃣':#3
                dic[userID]["speed"] = 150
            elif payload.emoji.name == '4️⃣':#4
                dic[userID]["speed"] = 200
            elif payload.emoji.name == '5️⃣':#5
                dic[userID]["speed"] = 250
            elif payload.emoji.name == '6️⃣':#6
                dic[userID]["speed"] = 300
            elif payload.emoji.name == '7️⃣':#7
                dic[userID]["speed"] = 350
            elif payload.emoji.name == '8️⃣':#8
                dic[userID]["speed"] = 400
            elif payload.emoji.name == '⬆️':#上
                if dic[userID]["speed"] <= 390:#200以上ダメ
                    dic[userID]["speed"] = dic[userID]["speed"] + 10            
            elif payload.emoji.name == '⬇️':#下
                if dic[userID]["speed"] >= 10:#0以下ダメ
                    dic[userID]["speed"] = dic[userID]["speed"] - 10
            else:
                return

        #感情
        elif payload.message_id == 827893199628402709:
            if dic[userID]["speaker"] == "show":
                await member.send("showくんに感情はありません")
                return

            if payload.emoji.name == '1️⃣':#1
                dic[userID]["emotion"] = "happiness"
            elif payload.emoji.name == '2️⃣':#2
                dic[userID]["emotion"] = "anger"
            elif payload.emoji.name == '3️⃣':#3
                dic[userID]["emotion"] = "sadness"
            elif payload.emoji.name == '4️⃣':#4
                #初期値＝削除
                try:
                    del dic[userID]["emotion"]
                    del dic[userID]["emotion_level"]
                except KeyError as e:
                    pass
            else:
                return

        #感情レベル
        elif payload.message_id == 827893261703446529:
            #データが存在しない場合は返信
            if "emotion" not in dic[userID]:
                await member.send("感情が設定されていません")
                return
            if payload.emoji.name == '1️⃣':#1
                dic[userID]["emotion_level"] = 1
            elif payload.emoji.name == '2️⃣':#2
                dic[userID]["emotion_level"] = 2
            elif payload.emoji.name == '3️⃣':#3
                dic[userID]["emotion_level"] = 3
            elif payload.emoji.name == '4️⃣':#4
                dic[userID]["emotion_level"] = 4
            else:
                return
        else:
            return

        msg = ""
        for k in dic[userID].items():
            msg = f"{msg}{k[0]}:{k[1]}\n"
        embed = discord.Embed(description=f"```{msg}```",color=0xff40ff)
        #embed.set_thumbnail(url=member.avatar_url)
        #embed.set_author(name="{}さんの設定".format(member.name),icon_url=self.bot.user.avatar_url)
        embed.set_author(name="{}さんの設定".format(member.name))

        await member.send(embed=embed)




    #特定のメッセージでリアクションが外れた時の動作
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
        guild = self.bot.get_guild(payload.guild_id) 
        member = guild.get_member(payload.user_id)
        #絵文字によって判定
        if payload.message_id == 827892914839355443:
            if payload.emoji.name == '1️⃣':#check
                ttsrole = guild.get_role(827887373106544682)
                await member.remove_roles(ttsrole)
                await member.send("TTSを外しました")
                return
            elif payload.emoji.name == '2️⃣':#2
                if member.voice is None:
                    await member.send('ボイスチャンネルに参加した上で、もう一度実行してください。')
                    return
                else:
                    vc = guild.voice_client
                    await vc.disconnect()
                    return
            else:
                return
        else:
            return



    @commands.command(aliases=['sum'])
    async def summon(self, ctx):
        if ctx.author.voice is None:
            await ctx.send('{} ボイスチャンネルに参加した上で、もう一度実行してください。'.format(ctx.author.mention))
            return
        else:
            vc = ctx.author.voice.channel
            await vc.connect()
            return
            
    @commands.command(aliases=['dis'])
    async def disconnect(self, ctx):
        if ctx.author.voice is None:
            await ctx.send('{} ボイスチャンネルに参加した上で、もう一度実行してください。'.format(ctx.author.mention))
            return
        else:
            vc = ctx.guild.voice_client
            await vc.disconnect()
            return


    @commands.command(aliases=['t'])
    async def tts(self,ctx):
        guild = self.bot.get_guild(piriko)
        ttsrole = guild.get_role(827887373106544682)
        if ttsrole in ctx.author.roles:
            await ctx.author.remove_roles(ttsrole)
            msg = await ctx.send("TTS消したよ")
        else:
            await ctx.author.add_roles(ttsrole)
            msg = await ctx.send("TTSつけたよ")
        await asyncio.sleep(5)
        await msg.delete()

    @commands.command(aliases=['de'])
    async def debug(self, ctx):
        global holdlist
        guild = self.bot.get_guild(piriko)
        await ctx.send("play:{}".format(guild.voice_client.is_playing()))
        await ctx.send("holdlist:{}".format(holdlist))


##########読み上げ設定##############

    #ループの作成
    @tasks.loop(seconds=1.5)
    async def mplayer(self):
        global holdlist
        #channel = self.bot.get_channel(659742326502981662)
        #await channel.send("test")
        guild = self.bot.get_guild(piriko)
        try:
            if guild.voice_client.is_playing() == False and len(holdlist) > 0:
                out = holdlist.pop(0)
                #await channel.send(out)
                #メッセージの内容を出力、再生。
                source = discord.FFmpegPCMAudio(out)
                guild.voice_client.play(source)
                #ソースファイルの削除
                #os.remove(out)
        except:
            pass

    @mplayer.before_loop
    async def before_mplayer(self):
        print('waiting...')
        await self.bot.wait_until_ready()
        

    #VC入退室時の処理
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after): 
        if member.bot:
            return
        
        guild = self.bot.get_guild(piriko)
        if guild.voice_client != None:
            pass
        else:
            return

        #ボッチになったら落ちる
        if len(guild.voice_client.channel.members) == 1:
            vc = guild.voice_client
            await vc.disconnect()
            return

        # ボイスチャンネルから退室
        if after.channel is None:
            msg = f'{member.name}が{before.channel.name}から退室しました'
        # ボイスチャンネルに参加
        elif before.channel is None and after.channel is not None:
            msg = f'{member.name}が{after.channel.name}に参加しました'
        # ボイスチャンネルを移動
        elif before.channel != after.channel:
            msg = f"{member.name}が{after.channel.name}に移動しました"
        else:
            return

        #メッセ送信者と同じボイスチャンネルなら
        if (guild.voice_client.channel == before.channel or guild.voice_client.channel == after.channel) and guild.voice_client.is_connected():


            global count
            global holdlist

            data = default.copy()
            
            #連番
            count = count + 1

            outfile = "out{}.wav".format(count)

            data["text"] = msg
            resp = requests.post(URL, params=data, auth=(key, ""))

            with open(outfile,'wb') as file:
                file.write(resp.content)

            #再生リストに追加
            holdlist.append(outfile)


                

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if "/" in message.content: 
            return
        if "）" in message.content: 
            return
        if ")" in message.content: 
            return
        if "@" in message.content: 
            return
        if ":" in message.content: 
            return
        if message.content.startswith("!"): 
            return
        if message.content.startswith("#"): 
            return
        if message.content.startswith("?"): 
            return
        if message.content.startswith("%"): 
            return
        if message.content.startswith("&"): 
            return
        if message.content.startswith("*"): 
            return
        if message.content.startswith("-"): 
            return
        
        #読み上げ条件
        if message.guild.voice_client != None:
            #botがボイスチャットにいる
            #メッセ送信者がボイスチャットにいる
            #メッセ送信者にTTSが含まれている
            #メッセ送信者と同じボイスチャンネル
            #メッセ送信チャンネルとボイスチャンネルのカテゴリが同じ
            if message.guild.voice_client.is_connected() and \
            message.author.voice and \
            (discord.utils.get(message.guild.roles, name="TTS") in message.author.roles) and \
            message.guild.voice_client.channel == message.author.voice.channel and \
            message.guild.voice_client.channel.category == message.channel.category:

                global count
                global holdlist
                global dic

                #テキストデータの編集。長文と「ｗｗ」
                texxxt = ""
                #長文だったら
                if len(message.content) > 40:
                    texxxt = message.content[:30] + "以下略"
                else:
                    texxxt = message.content

                #語尾ｗｗ
                if message.content.endswith("ww"):
                    texxxt = texxxt.rstrip('w') + "わらわら"
                elif message.content.endswith("ｗｗ"):
                    texxxt = texxxt.rstrip('ｗ') + "わらわら"
                elif message.content.endswith("w"):
                    texxxt = texxxt.rstrip('w') + "わら"
                elif message.content.endswith("ｗ"):
                    texxxt = texxxt.rstrip('ｗ') + "わら"

                #語尾顔文字
                if "（" in message.content or "(" in message.content:
                    texxxt = texxxt[:texxxt.find('(')]
                    texxxt = texxxt[:texxxt.find('（')] 

                #テキストデータの受け取り用id
                userID = str(message.author.id)

                #キーが存在しない場合は追加
                if userID not in dic:
                    dic[userID] = default.copy()
                
                #連番
                count = count + 1
                outfile = "out{}.wav".format(count)

                dic[userID]["text"] = texxxt
                print(dic[userID])
                resp = requests.post(URL, params=dic[userID], auth=(key, ""))

                with open(outfile,'wb') as file:
                    file.write(resp.content)

                #再生リストに追加
                holdlist.append(outfile)
                #メッセージの内容を出力、再生。ループに投げる
                #source = discord.FFmpegPCMAudio(outfile)
                #message.guild.voice_client.play(source)
                #os.remove(outfile)



def setup(bot):
    bot.add_cog(Speaker(bot))
