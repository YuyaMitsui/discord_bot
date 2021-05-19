
# インストールした discord.py を読み込む
import discord
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv

# 接続に必要なオブジェクトを生成
client = discord.Client()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@tasks.loop(seconds=60)
async def loop():
    now = datetime.now().strftime('%H:%M')
    yt = ["y","t"]
    if now == '19:25':
        await message.channel.send(random.choice(yt))
    await message.channel.send("test")
#ループ処理実行
loop.start()

# メッセージ受信時に動作する処理
# @client.event
# async def on_message(message):
#     # メッセージ送信者がBotだった場合は無視する

#     if message.author.bot:
#         return
#     command = message.content.split()
#     if command[0] == '/rand':
#         if len(command) == 3:
#             if command[1].isdigit() and command[2].isdigit():
#                 rand = random.randint(int(command[1]),int(command[2]))
#                 await message.channel.send(rand)
#             else:
#                 await message.channel.send("/rand min max\n[min,max]範囲の乱数生成")  
#         else:
#             await message.channel.send("/rand min max\n[min,max]範囲の乱数生成")   
#     if command[0] == '/randS':       
#         if len(command) > 2 :   
#             randlist = command[1:]
            
#             # await message.channel.send(randlist[0])
#             await message.channel.send(random.choice(randlist))
#         else:
#             await message.channel.send("/randS A B C D\n[A,B,C,D]の中からランダム")          

# Botの起動とDiscordサーバーへの接続
client.run(DISCORD_BOT_TOKEN)