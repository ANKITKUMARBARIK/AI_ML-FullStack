"""

By the end of this chapter, you will be able to:

• Understand the purpose and benefits of using functions
• Create reusable and modular code using def
• Improve readability, traceability, and maintainability with functions.
• Break down large tasks into smaller steps using well-named functions

"""


# Reducing Code Duplication
"""

You're managing a busy tea stall.

You receive many orders and want to print each customer's name along with the type of chai they ordered.

Task:
• Write a function print_order (name, chai_type)
• Call it multiple times for different customers

"""

def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} !")

print_order("John", "masala")
print_order("Sam", "ginger")
print_order("Alison", "tulsi")
