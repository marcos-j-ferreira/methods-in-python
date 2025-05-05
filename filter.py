
def basic():

    number = [1,2,3,4,5]
    

    func = lambda n: n % 2 ==0

    result = list(filter(func, number))

    print(result)

    #output: [2, 4]

basic()


def bigger0():

    number = [1,2,0,-3,-6]

    result = list(filter(lambda x: x > 0, number))

    print(result)

    #output: [1, 2]

bigger0()
