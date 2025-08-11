"""

A tea stall offers different prices for different cup sizes.

Write a program that calculates the price based on size.

Task:
• Input: "small", "medium", "large"
• Small → 10rs, Medium → 15rs, Large → 220rs
• If invalid: show "Unknown cup size"

"""

cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
    print(f"Price is 10 rupees")
elif cup == "medium":
    print(f"Price is 15 rupees")
elif cup == "large":
    print(f"Price is 220 rupees")
else:
    print(f"Unknown cup size")



"""

Delivery Charge Calculator----------->
You’re building a delivery system for an e-commerce platform. Depending on the distance of the customer’s address, different delivery charges apply.

Tasks:

- Take input from the user for delivery distance in Kilometers and store it in a variable named distance.
- If the distance is 2 km or less, return the string: "Delivery charge: 0"
- If the distance is greater than 2 km but not more than 5 km, return the string: "Delivery charge: 30"
- If the distance is greater than 5 km but not more than 10 km, return the string: "Delivery charge: 50"
- If the distance is more than 10 km, return the string: "Delivery not available for your location."

"""

# This function will be tested automatically. 
# Do not change the function name or parameter type.
def calculate_delivery_charge(distance: float) -> str:
    # Write your code below this line
    if distance <= 2:
        return "Delivery charge: 0"
    elif distance <= 5:
        return "Delivery charge: 30"
    elif distance <= 10:
        return "Delivery charge: 50"
    else:
        return "Delivery not available for your location."

print(f"{calculate_delivery_charge(5)}")
