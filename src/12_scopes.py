# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    global x 
    x = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()


'''
global var can be declared outside the function or in the globale scoop
so it can be reached in any where.
'''
'''
x  = "x"
def g():
    # x = x * 2 if we print this we will get an error
    # indicate that we can not  reference x before assignment
    # because python treated this as a local var


    # to make this work we need to declar x as a globale var
    # jut like the below code:
    global x
    x =  x * 2
    print(x)
g()
'''

'''
var declared inside the function called a local var
and cant be accessed outside of it
'''


# def outer():
#     x = "global to the function"

#     def inner():
#         nonlocal x # here we can manipulate the x 
#         x = "local to the outer function scoop but not for the try_local"
#         print(x)
#     inner()
#     print(x)

# outer()

