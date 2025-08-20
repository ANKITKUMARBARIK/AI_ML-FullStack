"""

Always remember, everything in python is an object...

even class is also an object itself.

"""


class Chai:
    pass


class ChaiTime:
    pass


print(type(Chai))

ginger_tea = Chai()  # object
print(f"{ginger_tea}")
print(f"{type(ginger_tea)}")

print(f"{type(ginger_tea) is Chai}")
print(f"{type(ginger_tea) is ChaiTime}")
