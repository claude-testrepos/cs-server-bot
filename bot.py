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


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Missing argument `{error.param.name}`. Try `!help {ctx.command}`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Bad argument, check `!help`")
    else:
        raise error


if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
