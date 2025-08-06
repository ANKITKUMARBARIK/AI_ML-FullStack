"""

You're building a ticket info system for a railway app.
Based on seat type, show its features.

Task:

• Input: "sleeper", "AC", "general", "luxury"
• Match using match-case
• Unknown → show: "Invalid seat type"

"""

seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print(f"Sleeper - No AC, beds available")
    case "ac":
        print(f"AC - AC conditioned, comfy ride")
    case "general":
        print(f"General - Cheapest option, no reservation")
    case "luxury":
        print(f"Luxury - Premium seat with meals")
    case _:
        print(f"Invalid seat type")



"""

Food Menu Selector----------------->
You’re creating a menu price lookup system for a digital food ordering app using the match-case statement.

Tasks:

- Define a function get_item_price that takes a string input item.
- Use match-case to return the following based on the item name:
"pizza" → "Price: 30 bucks"
"burger" → "Price: 15 bucks"
"pasta" → "Price: 20 bucks"
"salad" → "Price: 10 bucks"
- Any other item → "Item not available"
- Make sure the item check is case-insensitive (e.g., “BURGER” or “burger” should both match).

"""


# This function will be tested automatically. 
# Do not change the function name or parameter type.
def get_item_price(item: str) -> str:
    # write your code below this line
    items = item.lower()

    match items:
        case "pizza":
            return "Price: 30 bucks"
        case "burger":
            return "Price: 15 bucks"
        case "pasta":
            return "Price: 20 bucks"
        case "salad":
            return "Price: 10 bucks"
        case _:
            return "Item not available"

print(f"{get_item_price("BURGER")}")
