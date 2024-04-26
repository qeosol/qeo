# imports
from hikari.impl import SlashCommandBuilder
from typing      import Callable

# a custom command
# ----------------
# implemented for project control.
class Command(SlashCommandBuilder):
    call      : Callable
    owner_only: bool

    def __init__(self, name: str, description: str, o_o: bool, f: Callable):
        self.owner_only = o_o
        self.call       = f

        super().__init__(name, description)