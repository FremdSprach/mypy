"""
Variable Scopes in Python.

-- Global --
In Python, a variable declared outside of the function
or in global scope is known as global variable.
This means, global variable can be accessed
inside or outside of the function.

-- local --
Only visible within the method enclosure scope.

-- nonlocal --
Nonlocal variable are used in nested function
whose local scope is not defined. This means,
the variable can be neither in the local nor the global scope.
"""

var_global = 'global'


def use_global_variable():
    # Globals can be accessed from outside.
    print('var_global used from inside:', var_global)


def mod_global_variable():
    # Below is a wrong practice trying to modify
    # the value of a global variable.
    # var_global *= 2

    # Here is the right practice, we must use the 'global' modifier.
    global var_global
    var_global *= 2
    print('var_global *= 2:', var_global)


def use_local_variable():
    var_local = 'local'
    print('local variable used:', var_local)


global_local = 'both-global-local'


def global_local_same_name():
    global_local = 'both-local-global'
    print('global&local inside:', global_local)


def use_nonlocal_variable():
    x = 'local'

    def inner():
        # the scope of a nested method is not defined,
        # so x is in neither local nor global scope.
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)

    inner()
    print('outer:', x)
    # In the above code there is a nested function inner().
    # We use nonlocal keyword to create nonlocal variable.
    # The inner() function is defined in the scope of another outer function.
    #
    # Note : If we change value of nonlocal variable, the changes appears in the local variable.


def main():
    # global variable is visible within
    # both the outer-most scope and a method.
    use_global_variable()
    print('var_global used from outside:', var_global)

    # to modify a global variable inside a method,
    # the variable must be modified with the modifier 'global'.
    mod_global_variable()

    use_local_variable()

    # local variable is invisible from outside.
    try:
        # use of undefined (local)variables will raise NameError Exception.
        print(local_variable)
    except NameError as e:
        print(e)

    # global and local variables with the same name.
    global_local_same_name()
    print('global&local outside:', global_local)

    # nonlocal variables.
    use_nonlocal_variable()


if __name__ == '__main__':
    main()
