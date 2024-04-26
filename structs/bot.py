# imports
from hikari    import GatewayBot, Intents
from .unit     import Unit
from typing    import Sequence
from functools import partial

# for event indexing
import hikari

# a custom bot class
# ------------------
# handles event and command registration;
# implemented for project control.
class Bot(GatewayBot):
    units: Sequence[Unit]

    def __init__(self, **kwargs):
        self.units = []

        # add some client settings
        kwargs['intents'] = Intents.ALL
        kwargs['logs']    = None

        super().__init__(**kwargs)
    
    # add_unit()
    # ----------
    # adds a unit to the client's holder.
    def add_unit(self, u: Unit):
        # initiate unit reflection
        u.reflect()

        # add to the client's units
        self.units.append(u)
    
    # finalize()
    # ----------
    # resolves all necessary data for
    # the client to function properly.
    #
    # at the moment, it dynamically subscribes
    # to events using unit data.
    def finalize(self):
        # iterate through the client's units
        for u in self.units:
            # iterate through the unit's events
            for e in u.events:
                # get the matching hikari event type
                event = getattr(hikari, e.name + 'Event')

                # subscribe to the event
                self.subscribe(event, partial(e.call, u))