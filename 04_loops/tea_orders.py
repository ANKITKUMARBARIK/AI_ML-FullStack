"""

You receive a list of names for chai orders.

The goal is to print out the order queue.

Task:

• Use a list of names.
• Print: "Order ready for [name]"

"""


orders = ["John", "Sam", "Berlin", "Wick"]

for name in orders:
    print(f"Order ready for {name}")



"""

Task Completion Tracker-------------->
Instructions

You’re building a simple task tracker for a to-do app. Whenever a user completes tasks, your app should mark them as done.

Tasks:

- Define a function mark_completed_tasks that accepts a list of task names.
- Iterate through the list using a for loop, and update the format like "Completed:  {task}".
- Return a new list with the updated task strings.

"""


# This function will be tested automatically. 
# Do not change the function name or parameters.
def mark_completed_tasks(tasks: list[str]) -> list[str]:
    # Write your code below this line
    new_task = []
    for task in tasks:
        new_task.append(f"Completed: {task}")
    return new_task

print(f"{mark_completed_tasks(["day1","day2","day3"])}")
