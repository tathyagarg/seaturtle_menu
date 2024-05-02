==============
seaturtle_menu
==============

A quick and concise package to help you make terminal menus fast. It allows users to use custom bullet points that can wrap on overflow, as well as start at a given offset (like the numbers bulleting)

Ease of use:

.. code-block:: python

    >>> import seaturtle_menu as stm
    >>> menu = stm.menu.Menu(
    ...     stm.bullets.LOWERCASE_ALPHABET, {
    ...         'Say hello': lambda: print("Hello, World!"),
    ...         'Say bye': lambda: print("Bye, World!")
    ...     },
    ...     greeting='What will you choose?'
    ... )
    >>> menu.run()
    What will you choose?
    a. Say hello
    b. Say bye
    Choice:

Features
--------

- Write menus quickly
- Use custom bullets
- Code that warns you if you use incorrect types

Documentation
-------------

You can find the documentation of the 2 major objects here:

1. Menu can be found on :ref:`Menu <modules>`
2. Bullets can be found on :ref:`Bullets <bullets>`

Installation
------------

seaturtle_menu is available on PyPI, and can be installed by running the following command::

    $ python -m pip install seaturtle_menu

Or, get the source code from git::

    $ git clone https://github.com/tathyagarg/seaturtle_menu


License
-------

This project is licensed under the MIT license.