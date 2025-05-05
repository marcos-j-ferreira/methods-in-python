# methods-in-python
One review of some methods in Python, with a project for consolidating understanding.


# list-comprehension

Is a way to create lists using a concise syntax. It allows us to generate a new list by applying an expression to each item in an existing iterable (such as a list or range).
I've created a simple live example of using list comprehension, which is very important for practicing and efficiency in programming, and for making code more readable.

## Syntax of list comprehension

[expression for intem in iterable if condition]

# Zip 

The zip() function in Python combines multiple iterables such as list, tuples, strings, dict, into a single iterator of tuples. Each tuple contains elements from the input iterables that are at the same position.


## Syntax of zip()

zip(*iterables)

# Enumerate

Function adds a counter o each item in a list of other iterable. It turns the iterable into something we can loop through, where each item comes with its number (starting from 0 by default).

## Syntax of enumerate()

enumerate(iterable, start=0)

# Any

Python any() function returns True if any of the elements of a given iterable (list, dictionary, tuple, set, ect) are tuple elese is returns False

## Syntax of any()

any(iterable)

* Iterable: object such as a dictionary, tuple, list, set, etc.
*Returns:* Retuns True if any the items is True.

# All

The Python all() function returns true if all the elements of a given iterable (list, dictionary, tuple, set, etc) are True otherwise it return False. It also ruturns True if the iterable object is empty.

## Syntax of all()

all(iterable)

* Iterable: It is an iterable object such as a dictionaru, tuple, list, set

# Teste

Test config of git in local repository in my machine