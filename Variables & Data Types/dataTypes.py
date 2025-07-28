"""
numeric types:
int -> whole numbers 100, 200, -100
float -> decimal numbers 81.1, 10.65
complex -> real & imaginary part a+bj, 3+4j
"""
a = -100
b = 81.1
c = 3+4j
print(a,b,c)
print(type(a), type(b), type(c))  # display the type of data

"""
boolean types: True/False
"""
isVerified = True
isStatus = False
print(isVerified, isStatus)

"""
none types: None
"""
result = None
print(result)

"""
sequence types:
string - immutable
list - mutable
tuple - immutable
range
"""
details = "this is a string"
fruits = ["mango", "apple", "guava", 81, 81.5, True]
vegetables = ("Carrot","Pumpkin","Cabage",81,81.5,True)
print(details)
print(fruits)
print(vegetables)

"""
set types:
set - (mutable) unordered collection of unique items
frozenset - (immutable) unordered collection of unique items
"""
hobbies={"football", "volleyball", "basketball", "football", 81, 81.5, True}
skills=frozenset({"nodejs", "django", "postgresql", "reactjs","django", 81, 81.5, True})
print(hobbies)
print(skills)

"""
mapping types: dict - key : value 
"""
person={"username": "admin", "password": 123, 81: True}
print(person)
