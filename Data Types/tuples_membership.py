"""

Tuples are immutable

"""

masala_spices = ("cardamom","cloves","cinnamon")
print(f"{masala_spices}")

(spice1,spice2,spice3) = masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio} and C: {cadramom_ratio}")

# swap/flip the ratio (interesting)
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G: {ginger_ratio} and C: {cadramom_ratio}")


#membership
print(f"Is Ginger in masala spices {"cinnamon" in masala_spices}")

print(f"Is Ginger in masala spices {"cinnamon" not in masala_spices}")


"""

Swapping Temperature--------->
You are building a temperature converter app. Sometimes, due to incorrect input order, the min_temp and max_temp values are swapped.

Current values are:
min_temp = 40
max_temp = 25

Use Python tuples to swap them back to the correct order.

"""

min_temp = 40
max_temp = 25

min_temp, max_temp = max_temp, min_temp

print(min_temp)
print(max_temp)
