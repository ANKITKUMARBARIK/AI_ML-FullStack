# Improving Traceability
"""

Your shop adds a 10% VAT on every order.

You want this to be consistent and traceable.

Task:
• Write add_vat(price, vat_rate)
• Use it to compute final prices for 3 orders

"""


def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100


orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")


"""

Student Grading System-------------------->
You’re building an academic grading system.

Tasks:

- Define a function calculate_grade(score) that:
Returns “A” for score ≥ 90
“B” for ≥ 75
“C” for ≥ 60
“D” for ≥ 40
“F” otherwise
- Define a second function generate_student_report(name, score) that:
Uses the first function to determine the grade.
Returns a report string like: "Aman has scored 80 and received grade B"
- Write clean, reusable code using functions, conditions, and string formatting.

"""


def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def generate_student_report(name, score):
    grade = calculate_grade(score)
    return f"{name} has scored {score} and received grade {grade}"


print(f"{generate_student_report('Aman', 80)}")
