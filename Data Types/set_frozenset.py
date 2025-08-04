"""

Set - A set is a built-in Python data type used to store unique, unordered, and mutable items.

- Duplicates are automatically removed
- No indexing
- Great for mathematical operations (like union, intersection)

set types:
set - (mutable) unordered collection of unique items
frozenset - (immutable) unordered collection of unique items

"""


essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
# all_spices = essential_spices.union(optional_spices)
print(f"Union spices: {all_spices}")

common_spices = essential_spices & optional_spices
# common_spices = essential_spices.intersection(optional_spices)
print(f"Intersection spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
# only_in_essential = essential_spices.difference(optional_spices)
print(f"Only in essential spices: {only_in_essential}")


# membership
print(f"Only in essential spices: {"cloves" in essential_spices}")
print(f"Only in essential spices: {"cloves" not in essential_spices}")


# frozenset - immutable
skills=frozenset(["nodejs", "django", "postgresql", "reactjs","django", 81, 81.5, True])
print(f"{skills}")



"""

Managing Store Inventory------------->

You’re managing product categories for a retail store. Your task is to identify:-
Which products are available in which branches?
What products are common?
What products are missing in each branch?
And which products should not be altered using frozenset?

Tasks:

- Create a set branch_a_products with the items: "bread", "milk", "butter", "jam"
- Create another set branch_b_products with the items: "bread", "cheese", "butter", "ketchup"
Print both sets.
- Find and print the union of both branches’ products.
- Find and print the intersection of both branches’ products.
- Find and print the products that are in branch_a_products but not in branch_b_products.
- Check whether "ketchup" is available in branch_a_products and print the result.
- Define a frozenset called essential_items with values: "milk", "bread", "ketchup".
Print the frozenset.

"""

branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = {"bread", "cheese", "butter", "ketchup"}

print(f"{branch_a_products}")
print(f"{branch_b_products}")

print(f"{branch_a_products | branch_b_products}")

print(f"{branch_a_products & branch_b_products}")

print(f"{branch_a_products - branch_b_products}")

print(f"{'ketchup' in branch_a_products}")

essential_items = frozenset(["milk", "bread", "ketchup"])
print(f"{essential_items}")
