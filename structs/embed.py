# imports
from hikari import Embed as HikariEmbed

# for data loading
import json

# read data for image assets
with open('assets/images.json', 'r') as file:
    images = json.load(file)

class Embed(HikariEmbed):
    def __init__(self, **kwargs):
        # set our custom color
        kwargs['color'] = 0x2f3136
        
        super().__init__(**kwargs)

        # use our custom thumbnail
        self.set_thumbnail(images['thumb'])