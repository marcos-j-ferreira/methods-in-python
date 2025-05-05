
def basic():

    number = ['1','2','3','4','5']

    print(f"Matrix before the method is used : {number}")
    #output: ['1', '2', '3', '4', '5']

    result = list(map(int, number))

    print(f" after being used: {result}")
    #output: [1, 2, 3, 4, 5]

#basic()


def double():

    number = [2,4,8,16]

    two = lambda x: x * 2

    result = list(map(two, number))

    print(result)

    #output: [4, 8, 16, 32]

#double()

def upper():

    names = ["gabriel", "marcos", "ana", "luiza"]

    func = lambda c: c.upper()

    result = list(map(func, names))

    # or

    r = list(map(str.upper, names))

    print(result)
    print(r)

    #output: ['GABRIEL', 'MARCOS', 'ANA', 'LUIZA']

upper()

