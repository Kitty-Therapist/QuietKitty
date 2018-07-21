
import discord
import time
from discord.ext import commands

class announce:
    def __init__(self, bot):
        self.bot = bot
        self.running = True
    
    def __unload(self):
        self.running = False

    @commands.command()
    async def ping(self, ctx: commands.Context):
            """Shows the Gateway Ping"""
            t1 = time.perf_counter()
            await ctx.trigger_typing()
            t2 = time.perf_counter()
            await ctx.send(f":hourglass: Gateway Ping is {round((t2 - t1) * 1000)}ms :hourglass:")
            
    @commands.command(hidden=True)
    async def restart(self, ctx):
        """Restarts the bot"""
        await ctx.send("Restarting...")
        await self.bot.logout()
        await self.bot.close()

    @commands.command()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.guild_only()
    async def aria(self, ctx: commands.Context, *,aria = ""):
        channel= ctx.bot.get_channel(390300266244866049)
        role_id= 353539085723369502
        role= discord.utils.find(lambda r: r.id == role_id, ctx.guild.roles)
        if role is None:
            await ctx.send("Did you delete that role, <@186002153066725378>?")
            return

        if(aria != ""):
            try:
                await role.edit(mentionable=True)
                await channel.send(f"⸤ <@&353539085723369502> ⸣ {aria}\nGo here at https://www.twitch.tv/ariahane !\n\nIf you would like to un-/assign the role. Head on over to <#390296878773960705> and do ``_selfassign Aria's Stream``")
                await role.edit(mentionable=False)      
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the streaming channel. Please check that I am able to talk.")
        else: 
            await ctx.send("What are you doing? :(")

    @commands.command()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.guild_only()
    async def felics(self, ctx: commands.Context, *,felics = ""):
        channel= ctx.bot.get_channel(390300266244866049)
        role_id= 353539127561551872
        role= discord.utils.find(lambda r: r.id == role_id, ctx.guild.roles)
        if role is None:
            await ctx.send("Did you delete that role, <@186002153066725378>?")
            return 
            
        if(felics != ""):
            try:
                await role.edit(mentionable=True)
                await channel.send(f"⸤ <@&353539127561551872> ⸣ {felics}\nGo here at https://www.twitch.tv/felixinfintum !\n\nIf you would like to un-/assign the role. Head on over to <#390296878773960705> and do ``_selfassign Felics' Stream``")
                await role.edit(mentionable=False)      
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the streaming channel. Please check that I am able to talk.")
        else: 
            await ctx.send("What are you doing? :(")

    @commands.command()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.guild_only()
    async def joey(self, ctx: commands.Context, *,joey = ""):
        channel= ctx.bot.get_channel(390300266244866049)
        role_id= 421808313819463680
        role= discord.utils.find(lambda r: r.id == role_id, ctx.guild.roles)
        if role is None:
            await ctx.send("Did you delete that role, <@186002153066725378>?")
            return
            
        if(joey != ""):
            try:
                await role.edit(mentionable=True)
                await channel.send(f"⸤ <@&421808313819463680> ⸣ {joey}\nGo here at https://www.twitch.tv/goldmanjh !\n\nIf you would like to un-/assign the role. Head on over to <#390296878773960705> and do ``_selfassign Joey's Stream``")
                await role.edit(mentionable=False)      
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the streaming channel. Please check that I am able to talk.")
        else: 
            await ctx.send("What are you doing? :(")

    @commands.command()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.guild_only()
    async def rashaun(self, ctx: commands.Context, *,rashaun = ""):
        channel= ctx.bot.get_channel(390300266244866049)
        role_id= 447876832872890370
        role= discord.utils.find(lambda r: r.id == role_id, ctx.guild.roles)
        if role is None:
            await ctx.send("Did you delete that role, <@186002153066725378>?")
            return 
            
        if(rashaun != ""):
            try:
                await role.edit(mentionable=True)
                await channel.send(f"⸤ <@&447876832872890370> ⸣ {rashaun}\nGo here at https://www.twitch.tv/reshayshay !\n\nIf you would like to un-/assign the role. Head on over to <#390296878773960705> and do ``_selfassign Rashaun's Stream``")
                await role.edit(mentionable=False)      
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the streaming channel. Please check that I am able to talk.")
        else: 
            await ctx.send("What are you doing? :(")


    @commands.command()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.guild_only()
    async def ghoul(self, ctx: commands.Context, *,ghoul = ""):
        channel= ctx.bot.get_channel(390300266244866049)
        role_id= 456274504080031764
        role= discord.utils.find(lambda r: r.id == role_id, ctx.guild.roles)
        if role is None:
            await ctx.send("Did you delete that role, <@186002153066725378>?")
            return 
            
        if(ghoul != ""):
            try:
                await role.edit(mentionable=True)
                await channel.send(f"⸤ <@&456274504080031764> ⸣ {ghoul}\nGo here at https://www.twitch.tv/ghoulishfantasy !\n\nIf you would like to un-/assign the role. Head on over to <#390296878773960705> and do ``_selfassign Ghoul's Stream``")
                await role.edit(mentionable=False)      
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the streaming channel. Please check that I am able to talk.")
        else: 
            await ctx.send("What are you doing? :(")
    
    @commands.command()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.guild_only()
    async def shoutouts(self, ctx: commands.Context, *,shoutouts = ""):
        channel= ctx.bot.get_channel(390300266244866049)
        role_id= 439468306148360202
        role= discord.utils.find(lambda r: r.id == role_id, ctx.guild.roles)
        if role is None:
            await ctx.send("Did you delete that role, <@186002153066725378>?")
            return 
            
        if(shoutouts != ""):
            try:
                await role.edit(mentionable=True)
                await channel.send(f"⸤ <@&439468306148360202> ⸣ {shoutouts}\n\nIf you would like to un-/assign the role. Head on over to <#390296878773960705> and do ``_selfassign Shoutouts``!")
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the streaming channel. Please check that I am able to talk.")
        else: 
            await ctx.send("What are you doing? :(")
    
    @commands.command()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.guild_only()
    async def family(self, ctx: commands.Context, *,family = ""):
        channel= ctx.bot.get_channel(456233324269273129)
        role_id= 390303538288394240
        role= discord.utils.find(lambda r: r.id == role_id, ctx.guild.roles)
        if role is None:
            await ctx.send("Did you delete that role, <@186002153066725378>?")
            return 
            
        if(family != ""):
            try:
                await role.edit(mentionable=True)
                await channel.send(f"⸤ <@&390303538288394240> ⸣ {family}")
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the family announcement channel. Please check that I am able to talk.")
        else: 
            await ctx.send("What are you doing? :(")

def setup(bot):
    bot.add_cog(announce(bot))
