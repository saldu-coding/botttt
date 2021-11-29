import discord, datetime, asyncio, random, os #discord, datetime 모듈 불러오기
client = discord.Client() #client 설정

@client.event
async def on_ready(): #준비되었을때
    print('와 로그인 성공 샌주')
    print(client.user.name)
    print(client.user.id)
    print('====================================')

@client.event
async def on_message(message): #메세지를 보냈을때
    if message.content == "!잔여백신예약":
        await message.channel.send(random.choice(['잔여백신 예약을 성공하셨습니다. 알림톡을 확인하여주십시오.', '잔여백신이 마감되었습니다. 다시 시도해주세요.', '이런! 404오류 사이트가 응답하지 않습니다', '은근히 어려워요~ 날 쉽게 보지마~ 좀 힘 들어요~ 다시 시도 해줘요~', '또 안돼냐고 말하지 말아줘요, 같은사람 10000명 넘어요', '실패했단말에 남몰래 웃어요~']))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        embed=discord.Embed(color=0xff00, title="제목", description="설명", timestamp=message.created_at)
    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)
  
access token = os.environ["BOT_TOKEN"]
client.run(access_token) #token으로 봇을 실행한다
