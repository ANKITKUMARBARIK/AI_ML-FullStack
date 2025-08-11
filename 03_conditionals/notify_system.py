"""

You're creating a notification system for a smart kettle.

It should remind the user only when the kettle has finished boiling.

Task:
• A variable kettle_boiled = True
• If boiled, show: "Kettle done! Time to make chai!"

"""

kettle_boiled = True

if kettle_boiled:
    print(f"Kettle done! Time to make tea!")



"""

Customer Discount Eligibility-------->
You’re building a logic module for a billing system. Based on customer data, you need to evaluate whether they are eligible for a discount or a senior citizen privilege using if statements.

Tasks:

Create three variables:

customer_name = "Amit"
customer_age = 24
total_purchase = 1200

- If total_purchase is greater than 1000, print "Eligible for discount".
- If customer_age is greater than or equal to 60, print "Senior Citizen".

"""

customer_name = "Amit"
customer_age = 24
total_purchase = 1200

if total_purchase > 1000:
    print(f"Eligible for discount")
    
if customer_age >= 60:
    print(f"Senior Citizen")
    