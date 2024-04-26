# imports
from typing import Callable

# a custom event
# --------------
# made to hold event data;
# implemented for more project control.
class Event:
    name: str
    call: Callable

    def __init__(self, name: str, f: Callable):
        self.name = name
        self.call = f