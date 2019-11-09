import random

from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"pong ({round(self.bot.latency * 1000)}ms)")

    @commands.command()
    async def roll(self, ctx, sides: int = 6):
        await ctx.send(f"🎲 {random.randint(1, sides)}")

    @commands.command(name="8ball")
    async def eight_ball(self, ctx, *, question: str):
        answers = ["Yes.", "No.", "Ask again later.", "Definitely.", "Very doubtful."]
        await ctx.send(f"> {question}\n{random.choice(answers)}")


def setup(bot):
    bot.add_cog(Fun(bot))
