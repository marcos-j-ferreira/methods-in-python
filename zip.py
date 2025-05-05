def simple():

    # In this example, the function zip makes a list with the names and scores of people

    names = ["Marcos","Ana", "luiz", "Gabriel"]

    scores = [681,324,608]

    result = zip(names, scores)

    print(list(result))

    #output: [('Marcos', 681), ('Ana', 324), ('luiz', 608)]

#simple()

def different():

    # When the length is larger, but the number of elements is not equal, this new list has the number the elements that are in the two lists


    number = [1,2,3]
    letter = ['a', 'c']

    result = zip(number, letter)

    print(list(result))

    #output [(1, 'a'), (2, 'c')]

#different()

def unzipping():

    ziped = [(1,'a', (2, 'B'), (3, 'c'))]

    result = zip(*ziped)

    print(list(result))

#unzipping()

def creatingDictionary():

    keys = ['name', 'age', 'city']
    values = ['João', 30, 'New york']

    dictionary = dict(zip(keys, values))

    print(dictionary)

    # output: {'name': 'João', 'age': 30, 'city': 'New york'}

creatingDictionary()