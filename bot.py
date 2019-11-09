import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix="!")

for ext in ("cogs.fun", "cogs.study"):
    bot.load_extension(ext)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
