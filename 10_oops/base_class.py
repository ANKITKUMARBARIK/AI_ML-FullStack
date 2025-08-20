class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# # Code Duplication
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level


# # Explicit Call
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)  # explicit call
#         self.spice_level = spice_level


class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)  # call base class constructor
        self.spice_level = spice_level
