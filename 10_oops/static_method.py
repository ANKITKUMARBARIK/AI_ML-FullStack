class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]


raw = " water , milk , ginger , honey "

# obj = ChaiUtils()
# cleaned = obj.clean_ingredients(raw)
# print(cleaned)

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)
