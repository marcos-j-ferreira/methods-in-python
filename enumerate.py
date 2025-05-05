# This method is very simple, it is not necessary to make a long function how use, but a simple example to understand.


letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def with_for():

    for i, name in enumerate(letter, start=1):
        print(f"Index {i}: {name}")

with_for()

def with_simple():
    print(list(enumerate(letter, start=1)))

with_simple()
