from typing import Any

def verify_type[T](target: T | Any, expected: type):
    if isinstance(target, expected):
        return

    raise TypeError(f"Target: {target} expected to be of type: {expected}, found: {type(target)}")
