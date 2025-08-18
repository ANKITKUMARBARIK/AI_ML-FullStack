def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"


def imported_chai():
    yield "Matcha"
    yield "Oolong"


def full_menu():
    print("Welcome! What chai would you like ?")
    yield from local_chai()
    yield from imported_chai()


# chai = full_menu()
# print(f"{chai}")

# print(next(chai))
# print(next(chai))
# print(next(chai))
# print(next(chai))
# print(next(chai))

for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")


stall = chai_stall()

print(next(stall))
stall.close()  # cleanup


"""

Smart Token Dispenser-------------------->
You are developing a Smart Token Dispenser system, like those found in banks or clinics. This system reset counters based on user activity and needs to run until manually stopped.

Tasks:

Create an infinite generator function called token_dispenser(start=1).

On each call to next(), it should yield the current token number and increment it.

If a value is passed to the generator using send(), the generator should reset the token number to that new value.

The generator should handle the .close() method gracefully and print "Dispenser closed." when it is closed.

"""


def token_dispenser(start: int = 1):
    try:
        token = start
        while True:
            new_value = yield token
            if new_value:
                token = new_value
            else:
                token += 1
    except:
        print("Dispenser closed.")


dispenser = token_dispenser()
print(dispenser)

print(f"{next(dispenser)}")
print(f"{next(dispenser)}")
print(f"{next(dispenser)}")
print(f"{dispenser.send(10)}")
print(f"{next(dispenser)}")
print(f"{next(dispenser)}")

dispenser.close()
