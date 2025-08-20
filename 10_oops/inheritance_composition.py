"""

Inheritance: One class uses features of another ("is-a" relationship).

Composition: One class contains an object of another ("has-a" relationship).


"""


class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")


class MasalaChai(BaseChai):
    def add_spices(self):
        print(f"Adding cardamom, ginger, cloves.")


class ChaiShop:
    chai_cls = BaseChai  # hold reference of BaseChai class

    def __init__(self):
        self.chai = self.chai_cls("Regular")  # self.chai -> object

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()


class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()
print(shop.chai.type)
print(fancy.chai.type)
shop.serve()
fancy.serve()
fancy.chai.add_spices()  # !important
