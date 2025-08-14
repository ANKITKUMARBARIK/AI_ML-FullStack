"""

Comprehensions are a concise way to create
lists,
sets,
dictionaries,
or generators
in Python using a single line of code.

Types of Comprehensions:-
List, Set, Dictionary, Generator

[ expression for item in iterable if condition ]

"""

menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea",
]

iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)
