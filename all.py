#Like other methods, it is very simple. 

def basic():

    print(all([True, True, False]))

    # output: False, why is there a False in the list

    print(all([True, True, True]))

    # output: True, why are all elements true

#basic()

def long_array():

    array = [ 1,2,-3,8,-4,1,2,0]

    print(all(x > 0 for x in array))

#long_array()

def checkEven():

    number = [10,2,4,6]

    print(all(x % 2 == 0 for x in number))

#checkEven()