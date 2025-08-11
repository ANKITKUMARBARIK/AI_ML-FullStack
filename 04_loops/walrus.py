value = 13
remainder = value % 5

if remainder:
    print(f"Not divisible, remainder is {remainder}")



value = 13
if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")



available_sizes = ["small","medium","large"]

if (requested_size := input("Enter your tea cup size: ")) in available_sizes:
    print(f"Serving {requested_size} tea")
else:
    print(f"Size is unavailable - {requested_size}")



flavors = ["masala", "ginger", "lemon", "mint"]

print(f"Available flavors: {flavors}")

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} tea")
