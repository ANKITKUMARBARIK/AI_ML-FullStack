"""

You're building a smart thermostat alert system:

• If the device_status is "active"
• And temperature > 35 → Warn: "High temperature alert!"
• Else: "Temperature normal"
• If device is off → "Device is offline"

"""

device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print(f"High temperature alert!")
    else:
        print(f"Temperature is normal")
else:
    print(f"Device is offline")



"""

Loan Eligibility Checker-------------->
You’re building a basic loan eligibility checker for a bank. A customer must meet two conditions to be eligible:

Tasks:

- If the user’s age is 21 or above, check:
- If income is 25,000 Bucks or above, return: "Eligible for loan"
- Otherwise, return: "Not eligible: Income too low"
- If the user’s age is less than 21, return: "Not eligible: Age must be 21 or above"

"""


# This function will be tested by the evaluation system. Do not modify the function name or parameters.
def check_loan_eligibility(age: int, income: float) -> str:
    # Write your code below this line
    if age >= 21:
        if income >= 25000:
            return "Eligible for loan"
        else:
            return "Not eligible: Income too low"
    else:
        return "Not eligible: Age must be 21 or above"

print(f"{check_loan_eligibility(25, 50000)}")
