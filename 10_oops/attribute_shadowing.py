"""

In Python, instance attributes live in obj.__dict__ and class attributes live in Class.__dict__


"""


class Chai:
    # This is a class attribute (shared by all objects)
    temperature = "hot"
    strength = "Strong"


# Create an instance
cutting = Chai()

# Instance doesn't have its own 'temperature',
# so Python looks it up in the class
print(cutting.temperature)

# Now we assign a new attribute to the instance,
# this shadows (overrides) the class attribute
cutting.temperature = "Mild"
print(f"After changing: {cutting.temperature}")

# Class attribute is still unchanged
print(f"Direct look into the class: {Chai.temperature}")

# Delete the instance attribute
del cutting.temperature

# Now lookup happens again → not found in instance,
# so Python falls back to the class attribute
print(f"After deleting: {cutting.temperature}")

# Class attribute remains the same
print(f"Direct look into the class: {Chai.temperature}")
