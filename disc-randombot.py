
# インストールした discord.py を読み込む
import discord
import random
# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'THi5IsDuMMyaCCesSTOK3n00.Cl2FMQ.ThIsi5DUMMyAcc3s5ToKen0000'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    command = message.content.split()
    if command[0] == '/rand':
        if len(command) == 3:
            if command[1].isdigit() and command[2].isdigit():
                rand = random.randint(int(command[1]),int(command[2]))
                await message.channel.send(rand)
            else:
                await message.channel.send("/rand min max\n[min,max]範囲の乱数生成")  
        else:
            await message.channel.send("/rand min max\n[min,max]範囲の乱数生成")   
    if command[0] == '/randS':       
        if len(command) > 2 :   
            randlist = command[1:len(command)-1]
            await message.channel.send(random.choice(randlist))
        else:
            await message.channel.send("/randS A B C D\n[A,B,C,D]の中からランダム")          

# Botの起動とDiscordサーバーへの接続
client.run(DISCORD_BOT_TOKEN)