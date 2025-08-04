"""

Strings are immutable
- indexing
- slicing
- encoding

"""


tools_type = "Claude tool"
customer_name = "admin"

print(f"Order for {customer_name} : {tools_type} please !")


tool_description = "Aromatic and Bold"

print(f"First word: {tool_description[0]} and Last Word: {tool_description[len(tool_description) - 1]}")

print(f"First word: {tool_description[0:5]} and Last Word: {tool_description[7:len(tool_description) - 1]}")

print(f"First word: {tool_description[0:5:2]} and Last Word: {tool_description[len(tool_description) - 1]}")

print(f"First word: {tool_description[:5]} and Last Word: {tool_description[8:]}")


print(f"Word: {tool_description[::-1]}")  # reversing


label_text = "Department of BCA 🎓"
encoded_label = label_text.encode("utf-8")
print(f"Non encoded: {label_text}")
print(f"Encoded: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded: {decoded_label}")


"""

Should You Go for a Walk?
You’re deciding whether to go for a walk based on two real-life conditions:

is_sunny = True
have_umbrella = False

Print the result of the following:
Is it not sunny today?
Do you not have an umbrella?
Should you go for a walk if it’s sunny and you don’t need an umbrella?
Should you go for a walk if it’s sunny or if you have an umbrella?

"""

is_sunny = True
have_umbrella = False

print(f"{not is_sunny}")
print(f"{not have_umbrella}")
print(f"{is_sunny and not have_umbrella}")
print(f"{is_sunny or have_umbrella}")
