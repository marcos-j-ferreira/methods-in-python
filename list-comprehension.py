number = [1,2,3,4,5,6,7,8,9,10]


def sintax(x):

    # Basic syntax for making a simple comprehension 
    
    result = [value **2 for value in number]

    print(f"First array: {number}\nsecond array with comprehension {result}")

def with_condition(y, number):

    # syntax for comprehension with a condition

    if y == False:

        result_odd = [value for value in number if value  % 2 == 1]
        print(result_odd)
    else:
        result_even = [value for value in number if value % 2 == 0]
        print(f" Set of even: {result_even}")

y = True

#with_condition(y, number)

def creat_list(x):

    # Create a list with a range

    result = [i for i in range(x + 1)]

    print(result)

#creat_list(x=10)


def list3X3():
    
    result = [(x,z) for x in range(3) for z in range(3)]

    print(result)

    #output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

#list3X3()


def single_list():

    # Convert a matrix with rows into a single list

    mat = [[1,2,3],[4,5,6],[7,8,9]]

    result = [value for row in mat for value in row]

    print(result)

#single_list()


# Exercise

def upper_words():

    words = ["apple", "white", "wait", "hi"]

    result = [word.upper() for word in words]

    print(result)

upper_words()

