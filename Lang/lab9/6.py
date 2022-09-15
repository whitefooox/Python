from time import sleep
from discord.ext import commands
from config import D_TOKEN


class Bot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='timer')
    async def timer(self, ctx, seconds):
        sleep(int(seconds))
        await ctx.send("время X наступило!")

bot = commands.Bot(command_prefix='/')
bot.add_cog(Bot(bot))
bot.run(D_TOKEN)