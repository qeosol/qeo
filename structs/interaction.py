# imports
from hikari import CommandInteraction, ResponseType

# a custom interaction
# --------------------
# implemented for better control and
# cuter code overall.
class Interaction:
    raw: CommandInteraction

    def __init__(self, r: CommandInteraction):
        self.raw = r

    def __getattr__(self, attr):
        # get the attribute from the hikari data
        val = getattr(self.raw, attr, None)

        # if the hikari data had it, pass it
        if val is not None:
            return val
        
        # get the attribute from the custom data
        # (no recursionnnnnn!)
        val = self.__dict__.get(attr, None)

        return val

    # reply()
    # -------
    # implemented for cuter code; replies
    # to the interaction initially.
    async def reply(self, *args, **kwargs):
        # reply to said interaction
        await self.create_initial_response(
            ResponseType.MESSAGE_CREATE,
            *args, **kwargs
        )
    
    # edit_reply()
    # ------------
    # implemented for cuter code; edits the
    # originaly reply to the interaction.
    async def edit_reply(self, *args, **kwargs):
        # edit the reply to said interaction
        await self.edit_initial_response(*args, **kwargs)