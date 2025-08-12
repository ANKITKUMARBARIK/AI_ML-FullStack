"""

Types of functions:

- pure vs impure
- Recursive functions
- Lambdas (Anonymous function)

"""


def pure_chai(cups):
    return cups * 10


total_chai = 0


# not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups


# recursion
def pour_chai(n):
    # print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n - 1)


print(pour_chai(3))


# lambda
chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))
print(strong_chai)


"""

Function Types------------------------>
You're building a Function Behavior Analyzer to showcase different types of Python functions in action. Implement the following:

- Pure Function
Write a function pure_add(a, b) that takes two integers and returns their sum.
It should not rely on or modify any external state.

- Impure Function
Define a global variable counter.
Implement impure_increment() that increases the counter and returns its value.

- Recursive Function
Implement factorial_recursive(n) that returns the factorial of a given number using recursion.
Handle base case correctly (e.g., factorial_recursive(0) = 1).

- Lambda Function with map()
Write a function square_list(nums) that uses a lambda inside map() to return a new list with the squares of the numbers in the input list.

"""


def pure_add(a, b):
    return a + b


counter = 0


def impure_increment():
    global counter
    counter += 1
    return counter


def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def square_list(nums):
    return list(map(lambda num: num**2, nums))


print("Pure Function:", pure_add(5, 3))
print("Impure Function calls:")
print(impure_increment())
print(impure_increment())
print("Recursive Function (Factorial of 5):", factorial_recursive(5))
print("Lambda Function with map():", square_list([1, 2, 3, 4]))
