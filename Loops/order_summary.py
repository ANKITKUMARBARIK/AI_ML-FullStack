"""

You're preparing an order summary with customer names
and their total bill.

Task:
• Use two lists: one for names and one for bills.
• Print: "[Name] paid [amount]"

"""

names = ["john","sam","musk","sifra"]
bills = [12000,6000,10000,1800]

for name, bill in zip(names, bills):
    print(f"{name} paid {bill} rupees")



"""

Student Scores Report---------->
You’re building a simple student report generator that combines names and scores.

Tasks:

- Define a function generate_score_report that takes two lists — one with student names and one with their scores.
- Use the zip() function to pair each student with their score.
- Return a list of strings in the format "Name scored X marks"

"""


# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_score_report(names: list[str], scores: list[int]) -> list[str]:
    # Write your code below this line
    new_list = []
    
    for name, score in zip(names, scores):
        new_list.append(f"{name} scored {score} marks")
    return new_list

print(f"{generate_score_report(["ram","sam","kam"],[78,82,76])}")
