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
            reaction, user = await self.bot.wait_for_reaction(reactions, message=poll)

            reaction = str(reaction)

            react_hist[user] = None
            if reaction == "\N{FACE WITH TEARS OF JOY}":
                react_hist[user] = True
            elif reaction == "\N{POUTING FACE}":
                react_hist[user] = False
            else:
                await self.bot.say("yabba dabba doo")

            good_boys = "\n".join(boy.mention for boy, status in react_hist.items() if status == True)
            bad_boys = "\n".join(boy.mention for boy, status in react_hist.items() if status == False)
            dash = "\n" + "-"*30
            edit_string = f"@desu poker time?\n\ni play to win kid{dash}{good_boys}\n\npoker's for nerds{dash}{bad_boys}"

            await self.bot.edit_message(poll, new_content=edit_string)
            

def setup(bot):
    bot.add_cog(PokerPoll(bot))

