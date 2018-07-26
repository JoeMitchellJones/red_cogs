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
                playtime = dateutil.parser(playtime)
            except ValueError:
                await self.bot.say("wot fukin time is that diked?")
                return

        if ctx.message.channel.name != "poker":
            await self.bot.say("""bloodninja: Baby, I been havin a tough night so treat me nice aight?
BritneySpears14: Aight.
bloodninja: Slip out of those pants baby, yeah.
BritneySpears14: I slip out of my pants, just for you, bloodninja.
bloodninja: Oh yeah, aight. Aight, I put on my robe and wizard hat.
BritneySpears14: Oh, I like to play dress up.
bloodninja: Me too baby.
BritneySpears14: I kiss you softly on your chest.
bloodninja: I cast Lvl. 3 Eroticism. You turn into a real beautiful woman.
BritneySpears14: Hey…
bloodninja: I meditate to regain my mana, before casting Lvl. 8 Cock of the Infinite.
BritneySpears14: Funny I still don't see it.
bloodninja: I spend my mana reserves to cast Mighty F*ck of the Beyondness.
BritneySpears14: You are the worst cyber partner ever. This is ridiculous.
bloodninja: Don't f*ck with me bitch, I'm the mightiest sorcerer of the lands.
bloodninja: I steal yo soul and cast Lightning Lvl. 1,000,000 Your body explodes into a fine bloody mist, because you are only a Lvl. 2 Druid.
BritneySpears14: Don't ever message me again you piece of ****.
bloodninja: Robots are trying to drill my brain but my lightning shield inflicts DOA attack, leaving the robots as flaming piles of metal.
bloodninja: King Arthur congratulates me for destroying Dr. Robotnik's evil army of Robot Socialist Republics. The cold war ends. Reagan steals my accomplishments and makes like it was cause of him.
bloodninja: You still there baby? I think it's getting hard now.
bloodninja: Baby?""")
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

            if playtime >= datetime.datetime.now():
                time_to_duel = True
                if not instant:
                    await self.bot.say(f"@here its time to duel{self.dash}{good_boys}")


def setup(bot):
    bot.add_cog(PokerPoll(bot))
