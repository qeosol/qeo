from structs  import *
from decor    import command
from textwrap import dedent
import time

# an info unit
# ------------
# holds commands that provide useful
# information related to the client/project.
class InfoUnit(Unit):
    def __init__(self, bot):
        super().__init__(bot, 'info')
    
    @command('Ping, pong, ping.')
    async def ping(self, i):
        start_time = time.time()

        await i.reply('Pinging...')

        end_time = time.time()

        await i.edit_reply(dedent(
            f"""
                Response latency: `{round(((end_time - start_time) * 1000), 2)}ms`
                Heartbeat latency: `{round((self.bot.heartbeat_latency * 1000), 2)}ms`
            """
        ))

    @command('Sends the help menu.', options = [{
        'name'       : 'command',
        'description': 'A specific command you want info on.',
        'type'       : 'string'
    }])
    async def help(self, i):
        if i.options is not None:
            cname = i.options[0].value
            cmd   = None
            
            for u in self.bot.units:
                cmd = u.query(cname)
            
            if cmd:
                await i.reply(
                    Embed(
                        description = dedent(f"""
                            **{cmd.description}**
                            
                            Owner only: `{'☑️' if cmd.owner_only else '❌'}`
                            Is NSFW: `{'☑️' if cmd.is_nsfw else '❌'}`
                        """)
                    )
                )
            else:
                await i.reply('No command found.')
        else:
            embed = Embed()

            for u in self.bot.units:
                if u.name != 'events':
                    embed.add_field(
                        f'{u.name.title()} Commands',
                        ', '.join([f'`/{c.name}`' for c in u.commands.values()])
                    )

            await i.reply(embed)