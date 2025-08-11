"""

Lists are mutable

- alternate name something called Array, but in python we call List.

"""


ingredients = ["water","milk","black",]

ingredients.append("leaves")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

tea_ingredients = ["water","milk"]
spice_options = ["ginger","cardamom"]

tea_ingredients.extend(spice_options)
print(f"Tea ingredients are: {tea_ingredients}")

tea_ingredients.insert(2,"green")
print(f"Tea ingredients are: {tea_ingredients}")

last_removed = tea_ingredients.pop()
print(f"Tea ingredients are: {last_removed}")

print(f"Tea ingredients are: {tea_ingredients}")

tea_ingredients.reverse()
print(f"Tea ingredients are: {tea_ingredients}")

tea_ingredients.sort()
print(f"Tea ingredients are: {tea_ingredients}")

sugar_levels = [2,3,10,1,5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

print(f"Length of level: {len(sugar_levels)}")

print(f"Index of level: {sugar_levels.index(10)}")

print(f"Clear level: {sugar_levels.clear()}")



# Operator overloading
base_liquid = ["water","milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")


# convert string into list
str_list = "better than me"
str_list = str_list.split()
print(f"Str List: {str_list}")


# from operator import itemgetter

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINN", b"CARD")
print(f"Bytes: {raw_spice_data}")

print(f"Bytes: {raw_spice_data.decode("utf-8")}")



"""

Shopping List------------>
You’re building a shopping list feature in a grocery app. You need to support various list operations such as adding items, removing them, merging with others, and handling user inputs from text.

Tasks:

Create a grocery list named my_cart with the items: "apples", "bananas", and "milk"

- Print the grocery list.
- Add "bread" to the end of the list.
- Print the updated grocery list.
- Insert "ketchup" at the beginning of the list.
- Print the updated grocery list.
- Remove "bananas" from the list.
- Print the updated grocery list.
- Remove the last item from the list and store it in a variable named removed_item.
- Print the value of removed_item.
- Extend the grocery list by adding "rice" and "butter".
- Print the updated grocery list.
- Sort the grocery list in alphabetical order.
- Print the updated grocery list.
- Reverse the order of the grocery list.
- Print the updated grocery list.
- Concatenate the grocery list with another list containing "juice" and "jam".
- Print the resulting list.
- Duplicate the grocery list twice.
- Print the resulting list.
- Define a string with the value "tomato cucumber spinach" and convert it into a list.
- Print the converted list.

"""

my_cart = ["apples", "bananas", "milk"]

print(f"{my_cart}")

my_cart.append("bread")
print(f"{my_cart}")

my_cart.insert(0,"ketchup")
print(f"{my_cart}")

my_cart.remove("bananas")
print(f"{my_cart}")

removed_item = my_cart.pop()
print(f"{removed_item}")

my_cart.extend(["rice","butter"])
print(f"{my_cart}")

my_cart.sort()
print(f"{my_cart}")

my_cart.reverse()
print(f"{my_cart}")

concat_list = my_cart + ["juice", "jam"]
print(f"{concat_list}")

duplicated_cart = my_cart * 2
print(f"{duplicated_cart}")

str_list = "tomato cucumber spinach"
str_list = str_list.split()
print(f"{str_list}")
