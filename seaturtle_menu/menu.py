from typing import Callable, Any
from seaturtle_menu.utils import verify_type
from seaturtle_menu.consts import DEFAULT_ACTION
from seaturtle_menu.bullets import Bullets, Bulletable


class Menu:
    def __init__(
            self,
            _bullets: Bullets | Bulletable,
            action_prompt_map: dict[str, Callable | None],
            *,
            bracketing: str = '.',
            use_default_function: bool = False,
            input_converter: Callable[[str], str] = None,
            greeting: str = ''
    ) -> None:
        input_converter = input_converter or (lambda text: text)

        verify_type(use_default_function, bool)
        verify_type(action_prompt_map, dict)
        for k, v in action_prompt_map.items():
            verify_type(k, str)
            if v:
                verify_type(v, Callable)
            elif use_default_function:
                action_prompt_map[k] = DEFAULT_ACTION
            else:
                raise ValueError(
                    f"Expected Callable value as value for key = {k}, found {type(v)}. Use `use_default_function=True` to use a default function instead."
                )

        verify_type(_bullets, (Bullets, Bulletable))
        verify_type(input_converter, Callable)

        self.action_prompt_map = action_prompt_map
        self.prompts: list[str] = list(action_prompt_map.keys())
        self.actions: list[Callable] = list(action_prompt_map.values())
        if isinstance(_bullets, Bulletable):
            width: int = len(self.prompts)
            while width:
                width //= _bullets.charset_len

            width += 1
            self.width = width
            self.bullets = _bullets.from_width(self.width)
        else:
            self.width = _bullets.width
            self.bullets = _bullets

        self.bullets_as_list = list(self.bullets)[:len(self.prompts)]
        self.bracketing: str = bracketing
        self.converter: Callable[[str], str] = input_converter
        self.greeting = greeting

    def get_verified_input(self) -> str:
        """
        Gets user input that is guaranteed to be one of the bullets.

        Returns:
            A user choice that is in the bullets.
        """
        choice = input('>>> ')
        while choice not in self.bullets_as_list and \
                self.converter(choice) not in self.bullets_as_list:
            print('Invalid!')
            choice = input('>>> ')

        return self.converter(choice)

    def run(self) -> Any:
        """
        Runs the menu.
        Prints out the greeting, options, gets a verified user input, and performs the associated action.

        Returns:
            The value returned by the function associated to the user's choice.
        """
        if self.greeting:
            print(self.greeting)

        for bullet, prompt in zip(self.bullets, self.prompts):
            print(f'{bullet}{self.bracketing} {prompt}')

        choice: str = self.get_verified_input()
        return self.action_prompt_map[self.prompts[self.bullets_as_list.index(choice)]]()
