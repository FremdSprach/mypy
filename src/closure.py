"""
Question: What is a closure in Python? Write a simple example.

Below are instructions about Python closures from:
https://www.geeksforgeeks.org/python-closures/

---
Before seeing what a closure is, we have to first understand
what are nested functions and non-local variables.

A function which is defined inside another function is known as nested function.
Nested functions are able to access variables of the enclosing scope.
---

# Python program to illustrate nested functions.
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    innerFunction()

if __name__ == '__main__':
    outerFunction('Hey!')

As we can see innerFunction() can easily be accessed inside the outerFunction body
but not outside of it’s body. Hence, here, innerFunction() is treated as
nested Function which uses text as non-local variable.

-- Python Closure --
A Closure is a function object that remembers values in enclosing scopes
even if they are not present in memory.

#1, It is a record that stores a function together with an environment:
 a mapping associating each free variable of the function
 (variables that are used locally, but defined in an enclosing scope)
 with the value or reference to which the name was bound when the closure was created.
#2, A closure - unlike a plain function - allows the function to access
 those captured variables through the closure’s copies of their values or references,
 even when the function is invoked outside their scope.
#3, As observed from above code, closures help to invoke function outside their scope.
#4, The function innerFunction has its scope only inside the outerFunction.
 But with the use of closures we can easily extend its scope to invoke a function outside its scope.

-- When and why to use Closures --

#1, As closures are used as callback functions, they provide some sort of data hiding.
 This helps us to reduce the use of global variables.
#2, When we have few functions in our code, closures prove to be efficient way.
 But if we need to have many functions, then go for class (OOP).
"""
import logging

logging.basicConfig(level=logging.INFO)


# A very simple closure.
def outer(t):
    text = t

    def inner():
        print(text)

    return inner


# A more complicated one.
def logger(func):
    def logger_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))

    return logger_func


def add(x, y): return x + y


def sub(x, y): return x - y


def main():
    my_func = outer('Greetings!')
    my_func()

    add_logger = logger(add)
    sub_logger = logger(sub)

    add_logger(1, 2)
    sub_logger(1, 2)


if __name__ == '__main__':
    main()
