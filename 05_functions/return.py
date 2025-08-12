def make_chai():
    # return "Here is your masala chai"
    print("Here is your masala chai")


return_value = make_chai()
print(f"{return_value}")


def idle_chaiwala():
    pass


print(f"{idle_chaiwala()}")


def sold_cups():
    return 120


total = sold_cups()
print(f"{total}")


def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"


print(f"{chai_status(0)}")
print(f"{chai_status(4)}")


def chai_report():
    return 100, 20, 10  # sold, remaining


print(f"{chai_report()}")
sold, remaining, _ = chai_report()
print(f"{sold}")
print(f"{remaining}")
