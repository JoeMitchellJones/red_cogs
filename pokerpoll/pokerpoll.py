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
        poll = await self.bot.say("@desu poker time?\n\ni play to win kid\n\npoker's for nerds")

        for reaction in reactions:
            await self.bot.add_reaction(poll, reaction)

        good_boys = []
        bad_boys = []

        while True:
            reacts = await self.bot.wait_for_reaction(reactions, message=poll)

            if reacts.reaction == "\N{FACE WITH TEARS OF JOY}":
                if reacts.user in good_boys:
                    good_boys.remove(reacts.user)
                else:
                    bad_boys.remove(reacts.user)
                    good_boys.append(reacts.user)
            else:
                if reacts.user in bad_boys:
                    bad_boys.remove(reacts.user)
                else:
                    good_boys.remove(reacts.user)
                    bad_boys.append(reacts.user)

            edit_string = "@desu poker time?\n\ni play to win kid"
            for user in good_boys:
                edit_string += "\n"
                edit_string += user.mention
                edit_string += "\n\npoker's for nerds"
            for user in bad_boys:
                edit_string += "\n"
                edit_string += user.mention

            await self.bot.edit_message(poll, new_content=edit_string)
            

def setup(bot):
    bot.add_cog(PokerPoll(bot))

