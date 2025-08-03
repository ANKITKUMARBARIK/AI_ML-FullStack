"""

🔢 Numbers in Python
Python supports multiple numeric data types to represent different types of numbers.
They are all immutable, meaning their value can’t be changed in-place.

- Integers
- Booleans
- Real Numbers - Float, Decimal
- Complex - Used for complex numbers with real and imaginary parts. Rarely used in backend, more in scientific/math apps

+, -, *, /, //, %, **

"""


gold_grams = 14
diamond_grams = 3

total_grams = gold_grams + diamond_grams
print(f"Total Grams: {total_grams}")

remaining_grams = gold_grams - diamond_grams
print(f"Remaining Grams: {total_grams}")

milk_litres = 7
servings = 4

milk_per_serving = milk_litres / servings
print(f"Milk per serving: {milk_per_serving}")

total_tea_bag = 7
pots = 4
bag_per_pot = total_tea_bag // pots
print(f"Bag per pot: {bag_per_pot}")

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover C pods: {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"Scaled flavor strength: {powerful_flavor}")

total_leaves_harvested = 1_000_000_000  # readability
print(f"Tea leaves: {total_leaves_harvested}")
