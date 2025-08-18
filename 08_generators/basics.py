"""

Generators:-

A generator is a special type of iterator in Python.
It doesn’t store all values in memory at once. Instead, it creates values on the fly when you ask for them.

This makes generators memory-efficient and great for working with large data or infinite sequences.

you save memory
you don't want the results immedietely
lazy evaluation

"""


# generator func..
def serve_chai():
    yield "Cup 1: Masala chai"
    yield "Cup 2: Ginger chai"
    yield "Cup 3: Elaichi chai"


# stall just keeping a reference of serve_chai()
stall = serve_chai()
print(f"{stall}")

for cup in stall:
    print(f"{cup}")


# regular func..
def get_tea_list():
    return ["Cup 1", "Cup 2", "Cup 3"]


cup = get_tea_list()
print(f"{cup}")

for chai in cup:
    print(f"{chai}")


# Diff.. regular / generator func..
# regular func..
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]


# generator func..
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


chai1 = get_chai_list()
print(chai1)  # It creates the whole list at once and returns it.

chai2 = get_chai_gen()
print(chai2)  # yield means: "give one value and pause, continue from here next time"

print(next(chai2))
print(next(chai2))
print(next(chai2))
# print(next(chai2))  # gives error
