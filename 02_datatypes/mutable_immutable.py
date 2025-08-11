"""

🔍 In Python, when we say an object is immutable, we mean:
The object’s identity (memory address) changes when we try to modify it, not the value inside.

name = "chinu"
print(id(name))     # e.g., 123456

name += " dev"
print(name)         # "chinu dev"
print(id(name))     # different id (e.g., 7891011)



In Python, everything is an object, and each object has three key properties:
- Type
- Value
- Identity (Memory Address)

The main difference between mutable and immutable objects lies in how they behave in memory when modified.

✅ Immutable Objects
Immutable objects cannot be changed after they are created.
When you try to "change" them, Python creates a new object in memory, and the variable now points to this new memory address.

🔸 Examples: int, float, str, tuple, bool

a = "chinu"
print(id(a))      # memory id1

a += " dev"
print(id(a))      # different memory id2 → new object created

✔ Memory identity changed
✔ Value is new, but old object is untouched


✅ Mutable Objects
Mutable objects can be changed in-place after creation.
When modified, their identity (memory address) remains the same, but their internal state (value) gets updated.

🔸 Examples: list, dict, set

l = [1, 2, 3]
print(id(l))       # memory id1

l.append(4)
print(id(l))       # same memory id1 → object modified in-place

✔ Memory identity stays the same
✔ Only internal content changes

"""



# Immutable
firstName = "John"
print(f"First Name: {firstName} and ID: {id(firstName)}")

firstName += "Wilson"
print(f"Full Name: {firstName} and ID: {id(firstName)}")


# Mutable
serial_no = [1, 2, 3]
print(f"Serial No: {serial_no} and ID: {id(serial_no)}")

serial_no.append(4)
print(f"Serial No: {serial_no} and ID: {id(serial_no)}")


# PRACTICE
web_tools = set()
print(f"Initial Tools ID : {id(web_tools)}")

web_tools.add("claude")
web_tools.add("grok")
web_tools.add("perplexity")
print(f"Added Tools ID : {id(web_tools)}")
