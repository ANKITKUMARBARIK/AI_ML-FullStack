import recipes.flavors
print(recipes.flavors.ginger_chai())


from recipes.flavors import elaichi_chai
print(elaichi_chai())


from recipes.flavors import elaichi_chai as chai
print(chai())


from recipes.flavors import *
print(elaichi_chai())
print(ginger_chai())
