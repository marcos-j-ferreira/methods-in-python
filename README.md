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

# Sorted

Sorted() function returns a new sorted list from the elements of any iterable like (list, tuples, string). It creaes and returns a new sorted list and leaves the original iterable unchanged.

## Syntax of sorted()

sorted(iterable, key=None, reverse=False)

* Iterable: The sequence to be sorted. This can be a list, tuple, set, string, or any other iterable.
* Key (optional): A function to execute for deciding the order of elements. By default it is *None*
* reverse (optional): If *True,* sorts in descending order. Defaults value is *False* (ascending order)

# Lambda Functions

Python Lambda Functions are anonymous functions means that the function is without a name. As we already know the keyword is used to define a nomrmal function in Python. Similary, the lambda keyword is used to define an anonymous function in Python.

## Syntaxe of Lambda

* *lambda:* The keyword to define the function.
* *arguments:* A comma-separated list of input parameters (like in a regular function).
* *expression:* A single expression that is evaluated and returned.

# Map 

The map() is used to apply a given function to every item of an *iterable,* such as a list or tuple, and returns a *map object* (which is an iterator).

## Syntaxe of map

map(function, iterable)

*Parameter*

* *function:* The function we want to apply to every element of the iterable.
* *iterable:* The iterable whose elements we wnat to process.

* *note:* We can also pass multiple iterables if our function accepts multiple arguments.

# Filter

The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

## Syntaxe of filter

filter(function, sequence)

* *function:* A function that defines the condition to filter the elements. This function should return True for items you want to keep and False for those tou want to exclude.
* *iterable:* The iterable you wnat to filter

# Teste

Test config of git in local repository in my machine