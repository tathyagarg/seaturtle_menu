import string
from typing import Callable
from seaturtle_menu.utils import verify_type


class Bullets:
    def __init__(self, charset: str | list[str], *, start: int = 0, width: int = 1, allow_increase_width: bool = True) -> None:
        verify_type(charset, (str, list[str]))
        verify_type(start, int)
        verify_type(width, int)
        verify_type(allow_increase_width, bool)

        self.charset = list(charset)
        self.allow_increase_width = allow_increase_width
        self.width = width
        self.start = start

    def make_iter(self, width: int = 1) -> list[str]:
        """
        Make a list of bullets with the desired width.

        Args:
            width: The width of each bullet to return, in terms of bullet count.

        Returns:
            A list of bullets with the desired width

        Example usage:
            >>> Bullets('abc', width=2).make_iter(2)
            ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
        """
        if width == 1: return self.charset

        items: list[str] = self.make_iter(width - 1)
        result: list[str] = []

        for i, item in enumerate(items * len(self.charset)):
            result.append(self.charset[i // len(items)] + item)

        return result

    def __iter__(self) -> iter:
        iterator = iter(self.make_iter(self.width))
        start: int = self.start
        while start:  # skip the first 'self.start' number of bullets
            next(iterator)
            start -= 1

        return iterator


class Bulletable:
    """
    This class is used as an intermediate which is created before you know the desired width.
    """
    def __init__(self, maker: Callable[[int], Bullets], charset_len: int) -> None:
        self.maker = maker
        self.charset_len = charset_len

    def from_width(self, width: int) -> Bullets:
        """
        Make a Bullets object after you know the desired width.

        Args:
            width: The desired width of the Bullets object

        Returns:
            A Bullets object from the maker function with the given width.
        """
        return self.maker(width)


LOWERCASE_ALPHABET: Bulletable = Bulletable(maker=lambda width: Bullets(string.ascii_lowercase, width=width), charset_len=len(string.ascii_lowercase))
UPPERCASE_ALPHABET: Bulletable = Bulletable(maker=lambda width: Bullets(string.ascii_uppercase, width=width), charset_len=len(string.ascii_uppercase))
DIGITS: Bulletable = Bulletable(maker=lambda width: Bullets(string.digits, width=width, start=1), charset_len=len(string.digits))
