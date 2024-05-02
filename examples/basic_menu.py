"""
This example aims to show the basic working of menus.
"""

from seaturtle_menu.menu import Menu
from seaturtle_menu.bullets import DIGITS

def rectangle_area(x: int, y: int) -> None:
    print(f"Area is: {x * y}")

def rectangle_perimeter(x: int, y: int) -> None:
    print(f"Perimeter is: {2 * (x + y)}")

def get_xy_inputs() -> tuple[int, int]:
    return int(input("X: ")), int(input("Y: "))

def get_x_input() -> int:
    return int(input("X: "))

menu = Menu(
    DIGITS,
    {
        'Find rectangle area': lambda: rectangle_area(*get_xy_inputs()),
        'Find square area': lambda: rectangle_area(*([get_x_input()]*2)),
        'Find rectangle perimeter': lambda: rectangle_perimeter(*get_xy_inputs()),
        'Find square perimeter': lambda: rectangle_perimeter(*([get_x_input()]*2)),
        'Say bye': lambda: print('Bye!')
    },
    bracketing=')',
    greeting='Pick a choice: '
)

menu.run()

