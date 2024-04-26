# imports
from hikari.commands import *
from hikari.impl     import *
from structs.event   import *
from structs.command import *

# archetypes for enforcement
default_option = {
    'autocomplete'             : False,
    'channel_types'            : [],
    'choices'                  : [],
    'description'              : '',
    'description_localizations': {},
    'is_required'              : False,
    'max_length'               : None,
    'max_value'                : None,
    'min_length'               : None,
    'min_value'                : None,
    'name'                     : '',
    'name_localizations'       : {},
    'options'                  : None,
    'type'                     : OptionType.STRING
}

# a command decorator
# -------------------
# resolves basic data to a hikari slash command;
# implemented for more project control.
def command(
    description         : str,
    *,
    name                = None,
    name_locales        = {},
    description_locales = {},
    dm_allowed          = False,
    owner_only          = False,
    perms               = 0,
    nsfw                = False,
    options             = []
):
    def decor(f):
        # initiate the base for the command
        scmd = Command(
            name if name else f.__name__,
            description, owner_only, f
        )
        
        # set its necessary values
        scmd.set_name_localizations(name_locales)
        scmd.set_default_member_permissions(perms)
        scmd.set_description_localizations(description_locales)
        scmd.set_is_dm_enabled(dm_allowed)
        scmd.set_is_nsfw(nsfw)

        # iterate through its options
        for o in options:
            # create a default option structure instance
            dfi = dict(default_option)

            # add what values we have to the structure
            dfi.update(o)

            # handle the type assignment internally
            dfi['type'] = getattr(OptionType, dfi['type'].upper())

            # resolve all of this option's choices
            dfi['choices'] = [CommandChoice(**c) for c in dfi['choices']]

            # add this option to the command's composition
            scmd.add_option(CommandOption(**dfi))
        
        # pass the newly formed command
        return scmd

    return decor

# an event decorator
# ------------------
# syntax sugar for establishing a bot event.
def event(f):
    # break the function name down into parts
    parts = f.__name__.split('_')
    # assemble into titleized version
    name  = ''.join(p.title() for p in parts)

    # pass an event comprised of our parts
    return Event(name, f)