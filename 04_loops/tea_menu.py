"""

You're creating a tea menu board.

Each item must be numbered.

Task:

• Use enumerate() to print menu items with numbers.

"""

menu = ["green", "lemon", "spiced", "mint"]

for item in enumerate(menu, start=1):
    print(f"Menu item is {item}")

print("--------------------------------")

for idx, item in enumerate(menu, start=1):
    print(f"{idx} {item} tea")



"""

Numbered Task List-------------->
You’re improving the UX of a task management app by numbering the user’s task list automatically.

Tasks:

- Define a function generate_numbered_tasks that takes a list of task names.
- Use the enumerate() function to loop through the list with numbering starting from 1.
- Format each task as "1. Task Name" and return the final list.

"""

# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_numbered_tasks(tasks: list[str]) -> list[str]:
	# Write your code below this line
    new_tasks = []
    for idx, task in enumerate(tasks, start=1):
        new_tasks.append(f"{idx}. {task}")
    return new_tasks

print(f"{generate_numbered_tasks(["day1","day2","day3"])}")
