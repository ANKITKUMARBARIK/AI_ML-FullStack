"""

Scopes and Name Resolution

Local - inside a function
Enclosing from outer function if nested
global - Top level script
Built in

"""


def serve_chai():
    chai_type = "Masala"  # local scope
    print(f"Inside function {chai_type}")


chai_type = "Lemon"  # global scope
serve_chai()
print(f"Outside function {chai_type}")


def chai_counter():
    chai_order = "Lemon"  # enclosing scope

    def print_order():
        chai_order = "Ginger"
        print("Inner: ", chai_order)

    print_order()
    print(f"Outer: {chai_order}")


chai_order = "Tulsi"  # global scope
chai_counter()
print("Global: ", chai_order)
