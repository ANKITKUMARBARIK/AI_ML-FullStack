"""

Note:---
Each object has its own entity that called as namespaces..bcoz its doesn't affect other objects also doesn't affect the classes as well by default.

"""


class Chai:
    origin = "India"  # properties


# Chai.origin = "Russia"
print(Chai.origin)

Chai.is_hot = True  # add properties to this class
print(Chai.is_hot)

# creating objects from class Chai
masala = Chai()
print(masala)
print(f"Masala object: {masala.origin}")
print(masala.is_hot)
masala.origin = "Russia"
print(f"Masala object: {masala.origin}")


milk = Chai()
print(f"Milk object: {milk.origin}")
milk.origin = "UK"
print(f"Milk object: {milk.origin}")
milk.flavor = "Masala"
print(f"Milk object: {milk.flavor}")  # doesn't affect the class or other objects


# print(f"Chai Class/Object: {Chai.flavor}")  # class doesn't changed bydefault.. its like blueprint

print(f"Chai Class/Object: {Chai.origin}")
