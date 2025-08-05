"""

You run an online tea store.

If the order amount is more than > 300, delivery is free;
otherwise, it costs 230.

Task:
• Input: order_amount
• Use ternary operator to decide delivery fee

"""

order_amount = int(input("Enter the order amount: "))
# print(f"Order amount: {type(order_amount)}")

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees: {delivery_fees}")



"""

Age Verification System----------->
You’re building a system to verify user age for access.

Tasks:

- Define a function verify_age that accepts a string input named age_str.
- Convert age_str to an integer using int().
- Use a ternary operator to return:
- "Access Granted" if age is 18 or older
- "Access Denied" otherwise

"""

# This function will be tested automatically. 
# Do not change the function name or parameter type.
def verify_age(age_str: str) -> str:
    # Write your code here
    age = int(age_str)
    return "Access Granted" if age >= 18 else "Access Denied"

print(f"{verify_age(25)}")
