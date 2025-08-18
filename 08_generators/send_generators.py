def chai_customer():
    print("Welcome! What chai would you like ?")
    # order = yield
    while True:
        order = yield
        print(f"Preparing: {order}")


stall = chai_customer()
next(stall)  # start the generator

stall.send("Masala Chai")
stall.send("Ginger Chai")

"""

Step 1: Create generator
stall = chai_customer()  -This creates a generator object.

Function hasn’t run yet.
No output.

Step 2: Start generator
next(stall)  -The function starts running.

Prints:
Welcome! What chai would you like ?

Stops at order = yield, waiting for a value to come from .send().

Step 3: Send first order
stall.send("Masala Chai")

"Masala Chai" goes into order = yield.

So now order = "Masala Chai".

Inside the loop → prints:
Preparing: Masala Chai

Stops again at order = yield, waiting for the next order.

Step 4: Send second order
stall.send("Ginger Chai")

"Ginger Chai" goes into order = yield.

So now order = "Ginger Chai".

Inside the loop → prints:
Preparing: Ginger Chai

Stops again at order = yield.

"""
