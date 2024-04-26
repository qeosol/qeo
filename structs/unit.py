# imports
from typing      import Dict, Sequence
from hikari.impl import GatewayBot
from .event      import Event
from .command    import Command

# a data unit
# -----------
# holds command and event data; implemented to
# make data access more centralized.
class Unit:
    name    : str
    bot     : GatewayBot
    commands: Dict[str, Command]
    events  : Sequence[Event]

    def __init__(self, bot, name: str):
        self.bot      = bot
        self.name     = name
        self.commands = {}
        self.events   = []
    
    # reflect()
    # ---------
    # applies introspective programming to
    # collect data from unit instances.
    def reflect(self):
        # iterate through the unit's properties
        for el in self.__class__.__dict__:
            # get the current element as an attribute
            attr = getattr(self, el)


            # check if the element matches one of our types
            if isinstance(attr, Command):
                # add to the unit's data
                self.commands[attr.name] = attr
            elif isinstance(attr, Event):
                # add to the unit's data
                self.events.append(attr)
    
    # query()
    # -------
    # simply queries this unit for data
    # based on string input.
    def query(self, inp):
        # make an empty sequence for data
        data = []

        # add the unit's data to the sequence
        data.extend(self.commands.values())
        data.extend(self.events)

        # go through the data
        for v in data:
            # check if the value matches our query
            if v.name == inp:
                return v
        
        # nothing found ("T_T)
        return None