"""

Boolean: True/False, 1/0

Mostly used with logical operations: and, or, not

"""

is_status = True
is_status = 1

is_success = False
is_success = 0

str_count = 5

total_actions = is_status + str_count  # upcasting
print(f"Total actions: {total_actions}")

milk_present = 0
# milk_present = 1
# milk_present = "admin"
# milk_present = None
print(f"Is there milk? {bool(milk_present)}")


water_hot = True
leaves_added = False

can_serve = water_hot and leaves_added
print(f"Can serve? {can_serve}")



import sys
# from fractions import Fraction
# from decimal import Decimal as deci

ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temp: {ideal_temp}")
print(f"Current temp: {current_temp}")
print(f"Difference temp: {ideal_temp - current_temp}")  # in python precision is different
print(sys.float_info)
