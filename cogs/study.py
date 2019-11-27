import asyncio
import json
from pathlib import Path

from discord.ext import commands

DEADLINES = Path("deadlines.json")


def load():
    return json.loads(DEADLINES.read_text()) if DEADLINES.exists() else {}


def save(data):
    DEADLINES.write_text(json.dumps(data, indent=2))


class Study(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def deadline(self, ctx, course: str, date: str, *, what: str):
        """!deadline CS201 2019-11-20 assignment 3"""
        data = load()
        data.setdefault(course.upper(), []).append({"date": date, "what": what})
        save(data)
        await ctx.send(f"Saved: {course.upper()} {what} due {date}")

    @commands.command()
    async def deadlines(self, ctx):
        data = load()
        if not data:
            await ctx.send("No deadlines 🎉")
            return
        lines = []
        for course, items in sorted(data.items()):
            for it in sorted(items, key=lambda i: i["date"]):
                lines.append(f"**{course}** {it['date']} - {it['what']}")
        await ctx.send("\n".join(lines))

    @commands.command()
    async def done(self, ctx, course: str, *, what: str):
        """!done CS201 assignment 3"""
        data = load()
        items = data.get(course.upper(), [])
        remaining = [i for i in items if i["what"].lower() != what.lower()]
        if len(remaining) == len(items):
            await ctx.send("Couldn't find that one 🤔")
            return
        data[course.upper()] = remaining
        save(data)
        await ctx.send(f"Nice! Removed {course.upper()} {what} ✅")

    @commands.command()
    async def pomodoro(self, ctx, minutes: int = 25):
        await ctx.send(f"⏱ Focus for {minutes} minutes, {ctx.author.mention}!")
        await asyncio.sleep(minutes * 60)
        await ctx.send(f"⏰ Time for a break, {ctx.author.mention}!")


def setup(bot):
    bot.add_cog(Study(bot))
