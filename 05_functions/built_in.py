def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""  # should be first line
    chai = "ginger"
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)

help(len)

# documenting your function
def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return: (total amount, thank you message as string)
    """
    total = chai * 10 + samosa * 15
    return total, "Thank you for visiting."

print(generate_bill.__doc__)
print(generate_bill.__name__)
print(generate_bill(2,3))
