"""
Recursion is a programming technique where a function calls itself from within its own code,
In other words, a function is said to be recursive if it calls itself during its execution.



When a function is called recursively, it creates a new instance of itself with a new set of parameters, 
These new instances of the function can also call themselves, creating a chain of nested function calls that, 
continue until a certain condition is met. This is known as the base case and it is what stops the recursion
from continuing indefinitely.



Recursion is often used to solve problems that can be broken down into smaller subproblems,
Each recursive call solves a smaller subproblem until the base case is reached, at which point the results 
are combined to solve the original problem.


"""

# examples


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial)


""" Recursion like infinity stones , power that hold within 
if you dont use cautionsly it will cerate loops of destruction"""

# In other word it will destroy your project , dont use recursion with half knowledge u have to be cautions


"Recursion requires stroage and it is slow  but its important part of python "
# Recursion behaves like my  ex_girlfriend at some point


# To learn recursion i will use collab or juypter_notebook for meantime

