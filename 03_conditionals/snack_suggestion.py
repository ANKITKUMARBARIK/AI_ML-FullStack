"""

A local cafe wants a program that suggests a snack.
If a customer asks for cookies or samosa, it confirms the order.

Otherwise, it says it's not available.

Task:
• Take snack input
• If it's "cookies" or "samosa"
or "samosa", confirm the order
• Else, show unavailability

"""

snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print(f"Sorry, we only serve cookies or samosa with tea")



"""

Restaurant Billing System----------->
You’re designing a billing system for a restaurant. Depending on the total bill amount entered by the customer, they might get a free dessert.

Tasks:

- If the bill amount is greater than 500, return the string "You get a free dessert!"
- Otherwise, return the string: "No free dessert this time."

"""

# This function will be tested automatically. 
# Do not change the function name or parameter.
def get_delivery_offer(bill_amount: float) -> str:
    # # Write your code below this line
    # bill_amount = input("Enter your Bill Amount: ")
    if bill_amount > 500:
        return "You get a free dessert!"
    else:
        return "No free dessert this time."


print(f"{get_delivery_offer(600)}")
