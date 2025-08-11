"""

A chai shop makes tea in batches every 15 minutes.

You want to simulate 4 batches.

Task:
• Use range() to simulate batch numbers.
• Print: "Preparing chai for batch #[number]"

"""

for batch in range(1,5):
    print(f"Preparing tea for batch #{batch}")



"""

Generate Multiplication Table--------------->
You are developing a feature in an educational app that displays multiplication tables.

Tasks:

- Write a function named multiplication_table that takes a single integer argument number.
- Using a for loop and range(), generate the multiplication table for number from 1 to 10.
- Return a list of strings in the following format:
"number x i = result"
(Example: "3 x 4 = 12")

"""

# This function will be tested automatically. 
# Do not change the function name or parameter type.
def multiplication_table(number: int) -> list[str]:
    # Write your code below this line
    table = []
    for num in range(1,11):
        table.append(f"{number} x {num} = {number * num}")
    return table

print(f"{multiplication_table(3)}")
