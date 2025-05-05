

def basic():

    # will sort the matrix from smallest to largest

    number = [2,3,6,9,5,3,1]

    result = sorted(number)

    print(result)

    #output: [1, 2, 3, 3, 5, 6, 9]

#basic()


def key():
    
    fruits = ["strawbarry", "apple", "banana", "cherry","a2"]

    result = sorted(fruits, key=len)

    print(result)

    #output: ['a2', 'apple', 'banana', 'cherry', 'strawbarry']

key()

def sortingDictionaries():

    users = [
        {"name":"João", "score":69},
        {"name": "John", "score":80},
        {"name": "Eva", "score":71}
    ]

    result = sorted(users, key=lambda x: x['score'])

    print(result)

    # output: [{'name': 'João', 'score': 69}, {'name': 'Eva', 'score': 71}, {'name': 'John', 'score': 80}]

sortingDictionaries()

