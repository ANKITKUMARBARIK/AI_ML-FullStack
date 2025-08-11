"""

You want to simulate tea heating.

It starts at 40°C and boils at 100°C.

Task:
• Use a while loop.
• Increase temperature by 15 until it reaches or exceeds 100.
• Print each temperature step.

"""

temperature = 40

while temperature <= 100:
    print(f"Current temperature: {temperature}")
    temperature += 15

print("Tea is ready to boil")



"""

ATM Withdrawal Simulator----------------->
Imagine you’re building a backend feature for an ATM. Customers can request multiple withdrawals during one session. Your task is to simulate how the system should handle each request based on the account balance.

Tasks:

- Use a while loop to iterate through the list named withdrawals.
- For every withdrawal:
✅ If the current balance is enough:
Subtract the amount.
Append a success message: "Withdrawn: {amount}"
❌ If not enough:
Append a message: "Insufficient funds for requested amount: {amount}"
- After all withdrawals:
Append the final balance as: "Remaining Balance: balance"
- Return a list containing all the messages.

"""

# This function will be tested automatically. 
# Do not change the function name or parameters.
def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    # Write your code below this line
    new_lists = []
    balances = balance
    draw = 0
    while draw < len(withdrawals):
        if(balances >= withdrawals[draw]):
            balances -= withdrawals[draw]
            new_lists.append(f"Withdrawn: {withdrawals[draw]}")
        else:
            new_lists.append(f"Insufficient funds for requested amount: {withdrawals[draw]}")
        draw += 1
        
    new_lists.append(f"Remaining Balance: {balances}")
    
    return new_lists

print(f"{simulate_atm_withdrawals(15000,[1300,4000,300])}")
