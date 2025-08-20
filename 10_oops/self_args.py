"""

A function is independent, but a method is a function that belongs to a class.


"""


class Chaicup:
    size = 150

    # 'self' represents the current instance of the class (similar to 'this' in other languages).
    def describe(self):
        return f"A {self.size}ml chai cup"


cup = Chaicup()
print(cup)
print(cup.describe())

# Calling method via object passes 'self' automatically, but calling via class requires passing the object manually.
print(Chaicup.describe(cup))


cup_two = Chaicup()
cup_two.size = 100
print(cup_two.describe())
print(Chaicup.describe(cup_two))
