# Improving Readability
"""

You sell different chai sizes.

Instead of writing formulas everywhere, create a function.

Task:
• Write calculate_bill(cups, price_per_cup)
• Return total bill
• Use this function for multiple orders

"""


def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


my_bill = calculate_bill(2, 15)
print(my_bill)

print(f"Order for table 2: {calculate_bill(2, 15)}")

print(f"{calculate_bill(1, 15)}")
print(f"{calculate_bill(4, 15)}")
