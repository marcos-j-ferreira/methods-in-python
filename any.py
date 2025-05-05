# How is very simple in Python, does not require complex functions to understand, but a simple function


def simple():

    true = [True,True,True,True,True]
    false = [False, False]
    print(any(false))

#simple()

def anyWith_If():

    number = [4,5,6,7,8,9,10,38]

    print("Origin list: ", number)

    result = any(x > 10 for x in number)

    print("Does any element satisfy specified condition? :", result)

    #output: True, why 10 and 38 is bigger what 10

anyWith_If()