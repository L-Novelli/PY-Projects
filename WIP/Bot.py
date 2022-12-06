import discord
from discord.ext import commands
from discord.ext.commands import Bot
client = commands.Bot(command_prefix=":")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

@client.command()
async def rules(ctx):
    await ctx.send("the Admins Rules")

@client.command()
async def hi(ctx):
    await ctx.send("Hello admin team!")


@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)


@client.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_clients_in(server)
    await voice_client.disconnect()


@client.command(pass_context = True)
async def play(ctx, url, players):
    server = ctx.message.server
    voice_client = client.voice_clients_in(server)
    play = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()






client.run("")#token
