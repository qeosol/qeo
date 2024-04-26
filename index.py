# disable pycache
import sys

sys.dont_write_bytecode = True

# relevant imports
from structs import *
from units   import *

import json

# read data pertaining to the bot
with open('assets/app.json', 'r') as file:
    app = json.load(file)

# create a bot process
bot = Bot(token = app['token'])

# add the units
bot.add_unit(EventUnit(bot))
bot.add_unit(InfoUnit(bot))

# resolve bot data & run it
bot.finalize()
bot.run()