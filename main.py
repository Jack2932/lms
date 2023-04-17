import discord

from discord.ext import commands
import openai
import json

file = open('config.json','r')
config = json.load(file)

intents = discord.Intents.all()
bot = commands.Bot(config['prefix'], intents=intents)

openai.api_key = config['openai']
import openai


@bot.event
async def on_ready():
    print('Bot online')

@bot.command(name='gpt')
async def cont(ctx: commands.context, *, args):
    result = str(args)
    response = openai.Completion.create(

    model="text-davinci-003",
    prompt=result,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You"]
    )
    await ctx.send(embed=discord.Embed(title=f'{result}',description=response['choices'][0]['text']))

bot.run(config['token'])