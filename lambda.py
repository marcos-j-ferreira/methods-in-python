
def upperr():

    arguments = 'trêspratosdetrigoparatrêstigrestristes'

    funcao = lambda func: func.upper()

    print(funcao(arguments))

    # output: TRÊSPRATOSDETRIGOPARATRÊSTIGRESTRISTES

#upperr()

def conditionChecking():


    result = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

    print(result(10)) # positive
    print(result(-3)) # negative
    print(result(0))  # zero

#conditionChecking()


#exercie

def evenORodd():

    result = lambda x: "Even" if x % 2 == 0 else "Odd"

    print(result(6)) # Even
    print(result(5)) # Odd

#evenORodd()


