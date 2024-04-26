from structs import Unit, Interaction
from decor   import event
from hikari  import CommandInteraction

# an event unit
# -------------
# holds all the client's events/listeners.
class EventUnit(Unit):
    def __init__(self, bot):
        super().__init__(bot, 'events')
    
    @event
    async def started(self, data):
        commands = []

        for u in self.bot.units:
            commands.extend(u.commands.values())
        
        app = await self.bot.rest.fetch_application()

        await self.bot.rest.set_application_commands(
            application = app.id,
            commands    = commands
        )
    
    @event
    async def interaction_create(self, data):
        i = Interaction(data.interaction)

        if isinstance(i.raw, CommandInteraction):
            for u in self.bot.units:
                cmd = u.query(i.command_name)

                if cmd:
                    await cmd.call(u, i)