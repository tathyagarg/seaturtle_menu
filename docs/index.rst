==============
seaturtle_menu
==============

A quick and concise package to help you make terminal menus fast. It allows users to use custom bullet points that can wrap on overflow, as well as start at a given offset (like the numbers bulleting)

Ease of use:

.. code-block:: python
    :linenos:

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

