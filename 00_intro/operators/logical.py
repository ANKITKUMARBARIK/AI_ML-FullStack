"""
Logical operators - multiple conditions combine : True/False

and -> all conditions must be True
or -> at least one condition must be True
not -> single operand , reverse
"""

age = 20
isStudent = True

print(age>18 and isStudent)
print(age>25 or isStudent)
print(not isStudent)
print(not(age==20))
