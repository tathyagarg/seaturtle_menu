"""
This example shows how custom bullets are defined.
"""

from seaturtle_menu.menu import Menu
import seaturtle_menu.bullets as bullets

geeky_bullets = bullets.Bulletable(
    lambda width: bullets.Bullets(charset='01', width=width),
    charset_len=2
)

my_menu = Menu(
    _bullets=geeky_bullets,
    action_prompt_map={
        'simple hack': lambda: print('Your IP is idk i forgor, mb.'),
        'not so simple hack': lambda: print('Your IP is.. omg i still don\'t know.'),
        'script kiddie': lambda: print('This wasn\'t supposed to get your IP it was supposed to print this message uh huh.'),
        'super secret hacking alogrithm': lambda: print("You have been thoroughly hacked (trust)")
    },
    input_converter=lambda text: text.rjust(2, '0')
)

my_menu.run()
