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
 
    
# What is Factorial ?

"""
The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers 
less than or equal to n. For example, 5! = 5 × 4 × 3 × 2 × 1 = 120 . The value of 0! is defined as 1 .
Factorial is used in many areas of mathematics such as combinatorics, algebra, number theory, probability 
theory and mathematical analysis


# Lets undertand Factorial like a Dummies

Let’s say you have 3 toy cars and you want to line them up in a row. How many different ways can you do that?
Well, you can pick any of the 3 cars to be first in the row. Then, you have 2 cars left to pick from for the
second spot. Finally, there’s only 1 car left for the last spot. So, there are 3 × 2 × 1 = 6 different ways
to line up your toy cars.

This is what factorial is all about! It helps us find out how many different ways we can arrange things.
The factorial of a number is found by multiplying all the numbers from that number down to 1. So, the 
factorial of 3 is 3 × 2 × 1 = 6. We write it as 3! and say “3 factorial equals 6”




# Factorial defiend 0 ?

The factorial of 0 is defined as 1. This may seem strange at first, but it makes sense when you think
about it in terms of arranging things. If you have 0 things to arrange, there is only 1 way to do it -
by not arranging anything at all! So, 0! = 1.



 """
# Like this:
# n! = 1 * 2 * 3 * 4.....n

n = 4
product = 1

for i in range(n):
    product = product * (i + 1)
    print(product)


"""
How factorials work in recursion using Python ?


# For Dummmies #

 

Imagine you have a bunch of cookies and you want to know how many different ways you can arrange them on a 
plate. For example, with 3 cookies, you could arrange them as ABC, ACB, BAC, BCA, CAB, or CBA.

The number of different ways you can arrange the cookies is called the factorial, and it's written as an
exclamation mark after a number. For example, the factorial of 3 is written as 3!

Now, imagine you wanted to figure out the factorial of a really big number, like 10. It would take a 
long time to write out all the different arrangements of 10 cookies!

Instead, you can use recursion. Recursion is like a game of telephone, where one person tells the next person
what to do, and so on, until everyone has completed their task.

In the case of factorials, the function tells itself what to do, and keeps calling itself with a smaller 
number until it reaches the smallest number possible. Then, it uses all the results from the smaller numbers 
to calculate the final result.

So, to calculate the factorial of a number using recursion, you start with the original number and keep 
calling the function with a smaller number until you reach 1. Then, you use all the results from the smaller
numbers to calculate the final factorial.


"""

# In Python, a function to calculate the factorial using recursion might look like this:


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # prints 120, the factorial of 5


# The factorial function as before, and then calls the function with the argument 5 to calculate the
# factorial of 5. The result is then printed using the print() function.


# This function tells Python to multiply the original number by the factorial of the number one less than
# the original number. It keeps calling the function with a smaller number until it reaches 1, and then it
# uses all the results to calculate the final factorial.


"Lets Break this code in details how the previous code comes to its conclusion of output 120"

# The code defines a function called factorial that takes an integer n as its argument.
# The function uses recursion to calculate the factorial of n (i.e., the product of all positive integers up
# to and including n).

# Here's how the code works step by step:

# The factorial function is defined with an if statement that checks if n is equal to 1. If n is equal to 1,
# the function returns 1, because the factorial of 1 is 1.

# If n is not equal to 1, the else statement is executed. The function returns the product of n and the
# result of calling factorial(n-1). This is where recursion comes into play: the factorial function calls
# itself with the argument n-1, which means that the function will continue to call itself recursively with
# smaller values of n until it reaches the base case of n=1.

# Finally, the print() function is used to print the result of calling factorial(5), which calculates the
# factorial of 5 (i.e., 5 * 4 * 3 * 2 * 1 = 120).

# So, when the code is executed, the factorial function is called with the argument 5, which means that the
# function will use recursion to calculate the factorial of 5. The function will first call itself with the
# argument 4, then with the argument 3, then with the argument 2, and finally with the argument 1.At this
# point, the base case is reached, and the function returns 1. Then, the function will "unwind" and return
# the product of all the values it multiplied together,
# which is the factorial of 5 (i.e., 5 * 4 * 3 * 2 * 1 = 120).

# Finally, the print() function is used to print the result (i.e., 120) to the console.



 
