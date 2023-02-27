import nextcord
from nextcord.ext import commands
from craiyon import Craiyon
from PIL import Image
from io import BytesIO
import time
import base64
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="!", intents = nextcord.Intents.all())

@bot.event
async def on_ready():
    print("Bot funcionando, pesquise sua imagem!")

@bot.command()
async def generate(ctx: commands.Context, *, prompt: str):
    ETA = int(time.time() + 60)
    msg = await ctx.send(f"Isso vai demorar um pouco, sua imagem vai aparecer em <t:{ETA}:R>")
    generator  = Craiyon()
    result = generator.generate(prompt)
    images = result.images
    for i in images:
        image = BytesIO(base64.decodebytes(i.encode("utf-8")))
        return await msg.edit(content="Aqui está sua imagem!", file=nextcord.File(image, "generatedImage.png"))
    
bot.run(os.getenv('TOKEN')) 


