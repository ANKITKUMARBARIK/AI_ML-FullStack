# Hiding Implementation Details
"""

You're building a simple app that registers users.

You want to separate concerns: getting input, validating it, and saving it.

Task:
• Write register_user() that calls:
• get_input()
• validate_input()
• save_to_db()

"""

def get_input():
    print(f"Getting user input")

def validate_input():
    print(f"Validating the user info")

def save_to_db():
    print(f"Saving to database")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print(f"User registration complete")

register_user()
