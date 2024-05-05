.. _menu:

==============
The Menu Class
==============

class Menu(
    self,
    _bullets: Bullets | Bulletable,
    action_prompt_map: dict[str, Callable | None],
    *,
    restart_after_action: bool = False,
    bracketing: str = '.',
    use_default_function: bool = False,
    input_converter: Callable[[str], str] = None,
    greeting: str = ''
)