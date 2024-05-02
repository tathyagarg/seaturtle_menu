"""
This example intends to show the ability of the package to run nested menus, as well as to show off the working of the input_converter field
"""

from seaturtle_menu.menu import Menu
from seaturtle_menu.bullets import LOWERCASE_ALPHABET


def die():
    print("You died :(")


def raw_flesh():
    print('You contracted Salmonella.')
    die()


def north():
    print("You ran so fast that you didn't notice a cliff, and fell off.")
    die()

# Using `input_converter=str.lower` means that a user can input uppercase letters, and the package will recognize them as their lowercase counterparts.
parent = Menu(
    _bullets=LOWERCASE_ALPHABET,
    action_prompt_map={
        'Eat': Menu(
            _bullets=LOWERCASE_ALPHABET,
            action_prompt_map={
                'An Apple': lambda: print("You're nice and healthy now!"),
                'Raw Flesh': raw_flesh
            },
            greeting='What do you eat?',
            input_converter=str.lower
        ).run,
        'Run': Menu(
            _bullets=LOWERCASE_ALPHABET,
            action_prompt_map={
                'North': north,
                'South': lambda: print("You found a nice little town and now live a comfortable life!")
            },
            greeting='Where to?',
            input_converter=str.lower
        ).run,
        'Do nothing': die
    },
    bracketing=' ->',
    greeting='This is a tense situation. You are very hungry, and there are bees everywhere. What do you do?',
    input_converter=str.lower
)

parent.run()