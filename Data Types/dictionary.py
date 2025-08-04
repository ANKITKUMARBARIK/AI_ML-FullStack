"""

Dictionary - A dictionary is a collection of key-value pairs in Python.

"""

person_credentials = {"username": "admin", "password": 231}
print(f"Person: {person_credentials}")

tools_order = dict(type="AI model", version=4.5, status=True)
print(f"Tools: {tools_order}")

salad_recipe = {}
salad_recipe["name"] = "mix veg"
salad_recipe["liquid"] = "crud"

print(f"Recipe: {salad_recipe}")
print(f"Recipe name: {salad_recipe["name"]}")

del salad_recipe["liquid"]  # remove the key
print(f"Recipe: {salad_recipe}")


# membership
print(f"{'name' in salad_recipe}")


print(f"Person details (keys): {person_credentials.keys()}")
print(f"Person details (values): {person_credentials.values()}")
print(f"Person details (items): {person_credentials.items()}")

# last_item = person_credentials.pop("username")
last_item = person_credentials.popitem()
print(f"Person details (items): {last_item}")

extra_spices = {"cardamon": "crushed", "ginger": "sliced"}
salad_recipe.update(extra_spices)
print(f"Updated salad recipe: {salad_recipe}")

# recipe_size = salad_recipe["liquid"]  # app crashing (error)
recipe_size = salad_recipe.get("liquid", "NOT have liquid")
print(f"Recipe size: {recipe_size}")



"""

Customer Profile Management-------------------->
You are building a customer profile manager for a CRM (Customer Relationship Management) system. You need to store and manipulate customer data using Python dictionaries.

Tasks:

Create a dictionary named customer with the following fields:

- "name": "John Doe"
"age": 32
"city": "New York"
Print the dictionary.
- Add "email" and "phone" to the dictionary.
Print the updated dictionary.
- Print the customer’s "name" and "city" values.
- Check whether the key "email" exists in the dictionary and print the result.
- Delete the "age" field from the dictionary.
Print the updated dictionary.
- Print all dictionary keys, values, and items.
- Remove and print the last inserted key-value pair.
- Use .get() to access the key "membership" (which doesn’t exist).
Print the result.
- Update the dictionary with a new field "address" set to "221B Baker Street".
Print the final dictionary.

"""

customer = {"name": "John Doe", "age": 32 ,"city": "New York"}

print(f"{customer}")

customer["email"] = "john.doe@example.com"
customer["phone"] = "123-456-7890"
print(f"{customer}")

print(customer["name"])
print(customer["city"])

print(f"{'email' in customer}")

del customer["age"]
print(f"{customer}")

print(f"{customer.keys()} \n{customer.values()} \n{customer.items()}")

removed_field = customer.popitem()
print(f"{removed_field}")

membership = customer.get("membership")
print(f"{membership}")

customer.update({"address": "221B Baker Street"})
print(f"{customer}")
