# Being a first-class function allows for the function name to be
# reassigned (due to the name of the function holding a value) 


def Greeting():
    print("Hello there stranger!!!")

Hello = Greeting

Sup = Hello

Sup(); Hello()

# Can be used in other functions, list, dictionaries, whatever...


# All functions are variables. Therefore, their names can be reassigned
