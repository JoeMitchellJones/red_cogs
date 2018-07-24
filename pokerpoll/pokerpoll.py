import discord
from discord.ext import commands

class PokerPoll:
    """Cog that calls a vote to see who's playing poker"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pokerpoll",
                      aliases=["pp","poker"])
    async def poker_poll(self):
        """This does stuff!"""

        reactions = [
            "\N{FACE WITH TEARS OF JOY}",
            "\N{POUTING FACE}"
            ]

        #Your code will go here
        poll = await self.bot.say("@desu poker time?\n\ni play to win kid\n--------------------------\n\npoker's for nerds\n--------------------------")

        for reaction in reactions:
            await self.bot.add_reaction(poll, reaction)

        react_hist = {}

        while True:
            reacts = await self.bot.wait_for_reaction(reactions, message=poll)

            react_hist[reacts.user] = None
            if reacts.reaction == "\N{FACE WITH TEARS OF JOY}":
                react_hist[reacts.user] = True
            elif reacts.reaction == "\N{POUTING FACE}":
                react_hist[reacts.user] = False

            edit_string = "@desu poker time?\n\ni play to win kid\n--------------------------{}\n\npoker's for nerds\n--------------------------{}"
            edit_string.format("\n".join(boy for boy, status in react_hist.items() if status == True),
                              "\n".join(boy for boy, status in react_hist.items() if status == False))

            await self.bot.edit_message(poll, new_content=edit_string)
            

def setup(bot):
    bot.add_cog(PokerPoll(bot))

