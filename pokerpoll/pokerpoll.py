import datetime
import dateutil.parser
import discord
from discord.ext import commands


class PokerPoll:
    """Cog that calls a vote to see who's playing poker"""

    def __init__(self, bot):
        self.bot = bot
        self.dash = f"\n{'-'*32}\n"
        self.reactions = [
            "\N{FACE WITH TEARS OF JOY}",
            "\N{POUTING FACE}"
        ]

    @commands.command(name="pokerpoll", aliases=["pp", "poker"], pass_context=True)
    async def poker_poll(self, ctx, playtime="now"):
        """This does stuff!"""
        instant = False

        if playtime == "now":
            playtime = datetime.datetime.now() + datetime.timedelta(hours=1)
            instant = True
        else:
            try:
                playtime = dateutil.parser.parse(playtime)
            except ValueError:
                await self.bot.say("wot fukin time is that diked?")
                return

        if ctx.message.channel.name != "poker":
            await self.bot.say("""nope""")
            return

        #  Your code will go here
        poll = await self.bot.say("@here poker time?\n\n"
            f"i play to win kid {self.dash}"
            f"poker's for nerds {self.dash}")

        for reaction in self.reactions:
            await self.bot.add_reaction(poll, reaction)

        react_hist = {}
        time_to_duel = False

        def check(reaction, check_user):
            return not check_user.bot

        while not time_to_duel:
            reaction, user = await self.bot.wait_for_reaction(self.reactions, message=poll, check=check)

            react_hist[user] = None
            if reaction.emoji == "\N{FACE WITH TEARS OF JOY}":
                react_hist[user] = True
            elif reaction.emoji == "\N{POUTING FACE}":
                react_hist[user] = False
            else:
                await self.bot.say("yabba dabba doo")
                await self.bot.say(repr(reaction))
                await self.bot.say(reaction)
                await self.bot.say(user)

            good_boys = "\n".join(
                boy.mention for boy, status in react_hist.items() if status)
            bad_boys = "\n".join(
                boy.mention for boy, status in react_hist.items() if not status)

            edit_string = ("@here poker time?\n\n"
                f"i play to win kid {self.dash}{good_boys}\n\n"
                f"poker's for nerds {self.dash}{bad_boys}")

            await self.bot.edit_message(poll, new_content=edit_string)

            if playtime <= datetime.datetime.now():
                time_to_duel = True
                if not instant:
                    await self.bot.say(f"@here its time to duel{self.dash}{good_boys}")


def setup(bot):
    bot.add_cog(PokerPoll(bot))
