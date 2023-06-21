import json
import subprocess
import urllib
import random
import psutil
import os
import asyncio
import aiohttp
import discord
import requests
import time
import io
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from discord.ext import commands
from psutil import Process, virtual_memory

Color = ("green", "yellow", "red", "blue", "brown")
Color_list = list(Color)  # преобразуем кортеж в список
random_color = random.choice(Color_list)  # выбираем случайный цвет из списка

TOKEN = ""
TARGET_CPS = int(1500)
DELUXE_TARGET_CPS = int(10000)
DELUXE_ATTACK_TIME = int(120)
ATTACK_TIME = int(30)
METHODS = ["botjoiner", "ram", "mineping"]
METHODS_DELUXE = ["bighandshake", "bigpacket", "botjoiner", "botriad", "bungeedowner", "chatspam", "colorcrasher", "cpudowner", "doublejoin", "emptynames", "emptypacket", "extremejoin", "extremekiller", "handshake", "instantdowner", "invaliddata", "invalidnames", "invalidspoof", "ipspoofflood", "join", "legacyping", "legitnamejoin", "localhost", "longhost", "longnames", "memory", "motd", "nantibot", "nettydowner", "network", "newnullping", "nullping", "ping", "pingjoin", "query", "queue", "quitexceptions", "ram", "randomexceptions", "randompacket", "serverfucker", "slapper", "smartbot", "spoof", "tcpbypass", "tcphit", "ultimatekiller", "ultimatesmasher", "unexpectedpacket", "uuidcrash", "waterfallbypass", "xdjoin", "xdspam", "mineping"]
TITAN = ["bighandshake", "bigpacket", "botjoiner", "botriad", "bungeedowner", "chatspam", "colorcrasher", "cpudowner", "doublejoin", "emptynames", "emptypacket", "extremejoin", "extremekiller", "handshake", "instantdowner", "invaliddata", "invalidnames", "invalidspoof", "ipspoofflood", "join", "legacyping", "legitnamejoin", "localhost", "longhost", "longnames", "memory", "motd", "nantibot", "nettydowner", "network", "newnullping", "nullping", "ping", "pingjoin", "query", "queue", "quitexceptions", "ram", "randomexceptions", "randompacket", "serverfucker", "slapper", "smartbot", "spoof", "tcpbypass", "tcphit", "ultimatekiller", "ultimatesmasher", "unexpectedpacket", "uuidcrash", "waterfallbypass", "xdjoin", "xdspam", "mineping"]
OWNER = ["yoonikscry", "ultimatesmasher", "tcphit", "tcpbypass", "spamjoin", "serverfucker", "randombytes", "ram", "queue", "queryflood", "ping", "nullping", "network", "nettydowner", "nantibotcry", "longnames", "loginpingmulticrasher", "localhost", "legitnamekiller", "legitjoin", "ipspoofflood", "invalidnames", "handshakemethod", "extremejoin", "colorcrasher", "botnet", "botjoiner", "bigpacket", "bighandshake"] 
print("Бот сделан by Chearstern#3602")
DELUXE_NETTY = int(512)
DELUXE_LOOP = int(16)
NETTY = int(3)
LOOP = int(1)
slot = "TSLOT"
slot1 = "FSLOT"
slot11 = "FSLOT1"
slot2 = "DSLOT"
slot_slot = []
slot_slot1 = []
slot_slot2 = []
slot_slot11 = []

timebotter = commands.Bot(command_prefix='dd?', intents=discord.Intents.all())
timebotter.remove_command('help')
colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

@timebotter.command(name="Dattack")
async def DELUXE(ctx, host, proto, method, pon):
    if ctx.channel.id == 1088722900649005077:
        if method in METHODS_DELUXE:
            if slot2 == pon:
                if "zanet" not in slot_slot2:
                    slot_slot2.append("zanet")
                    args = ctx.message.content.split()[1:]
                    host, proto, method = args[0], args[1], args[2]
                    img = Image.open('lolibot.png')
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype('d9464-arkhip_font.ttf', 25)
                    draw.text((80, 60), f"Host: {host}", font=font, fill=(255, 0, 0))
                    draw.text((80, 100), f"Proto: {proto}", font=font, fill=(255, 0, 0))
                    draw.text((80, 140), f"Method: {method}", font=font, fill=(255, 0, 0))
                    draw.text((80, 180), f"Time: 30 sec", font=font, fill=(255, 0, 0))
                    draw.text((80, 220), f"Slot: DSLOT", font=font, fill=(255, 0, 0))
                    img.save('image2.png')
                    await ctx.channel.send(file=discord.File('image.png'))
                    time.sleep(1)
                    os.remove('image.png')
                    await asyncio.sleep(300)
                    id = slot_slot2.index("zanet")
                    slot_slot2.pop(id)
                else:
                    embed1 = discord.Embed(
                        title = "**SLOT IN COOLDOWN**",
                        description = "please, wait a 300 second or use other slot.",
                        color = discord.Colour.green()
                    )
                    await ctx.send(embed=embed1)
                    pass

            
                    
            
@timebotter.command(name="Fattack")
async def FREE(ctx, host, proto, method, pon):
    if ctx.channel.id == 1088722900649005077:
        if method in METHODS:
            if slot1 == pon:
                if "zanet" not in slot_slot1:
                    slot_slot1.append("zanet")
                    args = ctx.message.content.split()[1:]
                    host, proto, method = args[0], args[1], args[2]
                    img = Image.open('lolibot.png')
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype('d9464-arkhip_font.ttf', 25)
                    draw.text((80, 60), f"Host: {host}", font=font, fill=(255, 0, 0))
                    draw.text((80, 100), f"Proto: {proto}", font=font, fill=(255, 0, 0))
                    draw.text((80, 140), f"Method: {method}", font=font, fill=(255, 0, 0))
                    draw.text((80, 180), f"Time: 30 sec", font=font, fill=(255, 0, 0))
                    draw.text((80, 220), f"Slot: FSLOT", font=font, fill=(255, 0, 0))
                    img.save('image.png')
                    await ctx.channel.send(file=discord.File('image.png'))
                    time.sleep(1)
                    os.remove('image.png')
                    await asyncio.sleep(300)
                    id = slot_slot1.index("zanet")
                    slot_slot1.pop(id)
                else:
                    embed1 = discord.Embed(
                        title = "**SLOT IN COOLDOWN**",
                        description = "please, wait a 300 second or use other slot.",
                        color = discord.Colour.green()
                    )
                    await ctx.send(embed=embed1)
                    pass
            if slot11 == pon:
                if "zanet" not in slot_slot11:
                    slot_slot11.append("zanet")   
                    args = ctx.message.content.split()[1:]
                    host, proto, method = args[0], args[1], args[2]
                    img = Image.open('lolibot.png')
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype('d9464-arkhip_font.ttf', 25)
                    draw.text((80, 60), f"Host: {host}", font=font, fill=(255, 0, 0))
                    draw.text((80, 100), f"Proto: {proto}", font=font, fill=(255, 0, 0))
                    draw.text((80, 140), f"Method: {method}", font=font, fill=(255, 0, 0))
                    draw.text((80, 180), f"Time: 30 sec", font=font, fill=(255, 0, 0))
                    draw.text((80, 220), f"Slot: FSLOT (2)", font=font, fill=(255, 0, 0))
                    img.save('image.png')
                    await ctx.channel.send(file=discord.File('image.png'))
                    time.sleep(1)
                    os.remove('image.png')
                    await asyncio.sleep(300)
                    id1 = slot_slot11.index("zanet")
                    slot_slot11.pop(id1)
                else:
                    embed1 = discord.Embed(
                        title = "**SLOT IN COOLDOWN**",
                        description = "please, wait a 300 second or use other slot.",
                        color = discord.Colour.green()
                    )
                    await ctx.send(embed=embed1)
                    pass
                
                        
                        
@timebotter.command(name="Tattack")
@commands.has_role(1092121626780389396)
async def DELUXE(ctx, host, proto, method, pon):
    if ctx.channel.id == 1088722900649005077:
        if method in METHODS_DELUXE:
            if slot == pon:
                if "zanet" not in slot_slot:
                    slot_slot.append("zanet")
                    embed123 = discord.Embed(
                        title="**TSLOT**",
                        description=f"TSLOT STRESS HAVE BEEN LAUNCHED, {ctx.author.mention}",
                        color=discord.Colour.random()        
                    )

                    embed.add_field(name=' 📡 Server:', value=f'**{host}**', inline=True)
                    embed.add_field(name=' 🔰 Protocol:', value=f'**{proto}**', inline=True)
                    embed.add_field(name=' 🔗 Method:', value=f'**{method}**', inline=True )
                    embed.add_field(name=' 🕜 Time:', value=f'**{ATTACK_TIME}**', inline=True)
                    embed.add_field(name=' 🧬 Slot:', value=f'**TSLOT**', inline=True)
                    embed.set_image(url='https://media.giphy.com/media/C4NdKtRaQE9m8/giphy.gif')
                    await ctx.send(embed=embed123)
                    await asyncio.sleep(300)
                    id = slot_slot1.index("zanet")
                    slot_slot.pop("zanet")
                else:
                    embed21 = discord.Embed(
                        title = "**SLOT IN COOLDOWN**",
                        description = "please, wait a 300 second or use other slot.",
                        color = discord.Colour.green()
                    )
                    await ctx.send(embed=embed21)
                    pass
                

@timebotter.command(name="mineping")
async def FREE(ctx, host, port, pon):
            if slot1 == pon:
                if "zanet" not in slot_slot1:
                    slot_slot1.append("zanet")
                    await asyncio.sleep(10)
                    embed123 = discord.Embed(
                        title="**FSLOT**",
                        description=f"FSLOT STRESS HAVE BEEN LAUNCHED, {ctx.author.mention}",
                        color=discord.Colour.random()        
                    )

                    embed123.add_field(name=' 📡 Server:', value=f'**{host}:{port}**', inline=True)           
                    embed123.add_field(name=' 🔗 Method:', value=f'**mineping**', inline=True )
                    embed123.add_field(name=' 🕜 Time:', value=f'**{ATTACK_TIME}**', inline=True)
                    embed123.add_field(name=' 🧬 Slot:', value=f'**FSLOT**', inline=True)
                    embed123.set_image(url='https://media.tenor.com/VWQBHy0kZW4AAAAC/anonymous-guy-fawkes.gif')
                    await ctx.send(embed=embed123)
                    await asyncio.sleep(300)
                    id = slot_slot1.index("zanet")
                    slot_slot1.pop(id)
                else:
                    embed21 = discord.Embed(
                        title="**SLOT IN COOLDOWN**",
                        description="Please wait for 300 seconds or use another slot.",
                        color=discord.Colour.green()
                    )
                    await ctx.send(embed=embed21)
                    pass  


                 

@timebotter.command(aliases=['avt'])
@commands.has_role(1092116704529764404)
async def avatar(ctx, *, member: discord.Member = None):
    member = ctx.author if not member else member 
    embed = discord.Embed(title = f"{member.name}'s Аватар:", color=random.choice(colors) , timestamp= ctx.message.created_at)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"LoliBot | Chearstern#3602")
    await ctx.send(embed=embed)

@avatar.error
async def mycommand_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('У вас нет прав на это')


@timebotter.command(name="clear")
@commands.has_role(1092116704529764404)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
   if amount == None:
       await ctx.channel.purge(limit=1000000)
   else:
       await ctx.channel.purge(limit=amount)

@clear.error
async def mycommand_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('У вас нет прав на это')





@timebotter.command(name='portscan')
async def posss(ctx, arg1):
  if ctx.channel.id == 1088722900649005077:
    if arg1 == 'myipwashere!':
     await ctx.send("Неправильный айпи!")
    else:
       async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.viewdns.info/portscan/?host={arg1}&apikey=629e5c64f2ca88c1652e746b083af35a06cc57bb&output=json") as r:
                       if r.status == 200:
                        text = await r.text()
                        embed1 = discord.Embed(title=(f'Результаты: {arg1}'), description=(text), color=discord.Color.from_rgb(0, 191, 255))
                        await ctx.send(embed=embed1)
                       else:
                           erroremb = discord.Embed(title="Была допущена ошибка!",
                                                    description="API, скорее всего, не работает, свяжитесь с Chearstern#3602",
                                                    colour=discord.Colour.red())
                           await ctx.send(embed=erroremb)




@timebotter.command()
async def botping(ctx):
  if ctx.channel.id == 1088722900649005077:
    await ctx.send("Пинг Бота: **{0}ms**".format(round(timebotter.latency * 1000)))

@timebotter.command()
@commands.has_role(1092116704529764404)
async def kick(ctx, member: discord.Member, reason="Нету причины."):
    await ctx.send(f"{member.mention} Был кикнут. | Причина: {reason}")
    await member.kick(reason=reason)

    
@timebotter.command()
@commands.has_role(1092116704529764404)
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason="нету причины"
    await ctx.guild.ban(member)
    await ctx.send(f'участник {member.mention} был кикнут за {reason}')
@timebotter.command()
@commands.has_role(1092116704529764404)
async def unban(ctx, member: discord.Member):
    await ctx.send(f"{member.mention} был разбанен.")
    await member.unban()



           


            



            

@timebotter.command()
@commands.has_role(1092116704529764404)
async def stats(ctx):
    memoryused = round(psutil.virtual_memory().used / 1000000000, 2)
    memory = f"{memoryused}GB"
    embed = discord.Embed(title = '𝗦𝘆𝘀𝘁𝗲𝗺 𝗥𝗲𝘀𝗼𝘂𝗿𝗰𝗲 𝗨𝘀𝗮𝗴𝗲:', description = '')
    embed.add_field(name = 'CPU Usage:', value = f'{psutil.cpu_percent()}%', inline = False)
    embed.add_field(name= 'RAM Usage:', value=memory)
    embed.add_field(name = 'Memory Usage:', value = f'{psutil.virtual_memory().percent}%', inline = False)
    embed.add_field(name = 'Available Memory:', value = f'{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%', inline = False)
    await ctx.send(embed = embed)       



@timebotter.command()
async def help(ctx):
    embed = discord.Embed(
        title=":zap:𝙃𝙀𝙇𝙋:zap:",
        color=discord.Colour.green(), timestamp= ctx.message.created_at
    )
    
    embed.add_field(name=f'***MENU***:', value='**dd?iplookup** >> IP детали \n **dd?pinghost** >> пинг жертвы \n **dd?botping** >> пинг бота \n **dd?stop** >> остановить все атаки(оффнуть все дедики) dd?AttackHelp >> там рассписаны кпс, слоты, как атаковать и т.п ')

    embed.set_thumbnail(
        url=''
    )
    #https://media.giphy.com/media/U4FkC2VqpeNRHjTDQ5/giphy-downsized-large.gif
    embed.set_image(url=f'https://cdn.discordapp.com/attachments/964800182980059149/988360082033082368/standard.gif')
    embed.set_footer(text="LoliBot | Chearstern#3602")
        
    await ctx.send(embed=embed)




@timebotter.command()
async def iplookup(ctx, arg1):
    url = "http://ipwhois.app/json/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="IP Resolver",
        color=discord.Colour.green() , timestamp= ctx.message.created_at
    )
    embed.add_field(name="Ip:", value=json_object["ip"], inline=False)
    embed.add_field(name="Type:", value=json_object["type"], inline=False)
    embed.add_field(name='Continent:', value=json_object["continent"], inline=False)
    embed.add_field(name="Region:", value=json_object["region"], inline=False)
    embed.add_field(name="Country:", value=json_object["country"], inline=False)
    embed.add_field(name="City:", value=json_object["city"], inline=False)
    embed.add_field(name="Latitude:", value=json_object["latitude"], inline=False)
    embed.add_field(name="Longitude:", value=json_object["longitude"], inline=False)
    embed.add_field(name="Timezone:", value=json_object["timezone_gmt"], inline=False)
    embed.add_field(name="ISP:", value=json_object["isp"], inline=False)
    embed.add_field(name="Org:", value=json_object["org"], inline=False)
    embed.add_field(name="ASN:", value=json_object["asn"], inline=False)
    embed.set_footer(text="LoliBot | Chearstern#3602")
    embed.set_image(url=f'https://cdn.discordapp.com/attachments/964800182980059149/988360082033082368/standard.gif')
    await ctx.send(embed=embed)

    




        
    
 

@timebotter.command()
@commands.has_role(1092116704529764404)
async def stop(ctx):
    os.system("pkill 'java'")
    embed = discord.Embed(
        title='**Все дедики были оффнуты!**',
        color=discord.Colour.green()
    )
    embed.set_image(url=f'')
    embed.set_footer(text="LoliBot | Chearstern#3602")
    await ctx.send(embed=embed)


@DELUXE.error
async def mycommand_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(title="ДОСТУП К DSLOT or TSLOT НЕ КУПЛЕН", description="Что бы пользыватся DSLOT, TSLOT слотами, преобретайте его у Chearstern#3602", color=discord.Colour.random())
        await ctx.send(embed=embed)


@timebotter.command()
async def pinghost(ctx, arg1):
    url = "https://steakovercooked.com/api/ping/?host=" + arg1
    response = requests.get(url, verify=True) 
    await ctx.send(response.json())


   
      


@timebotter.event
async def on_ready():
    await timebotter.change_presence(status=discord.Status.online, activity=discord.Game("LoliDDoS | Chearstern"))

timebotter.run('MTA5MzkyOTc3NDA4ODQ3NDY0NA.GzWGQh.XipNeuzbVzZKfQ220JTDp1MYo5Cfg66PQUGXhE')