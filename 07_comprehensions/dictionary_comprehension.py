"""

{ expression for item in iterable if condition }

"""

tea_prices_inr = {"Masala chai": 40, "Green Tea": 50, "Lemon Tea": 200}

tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}
# tea_prices_usd = {tea: f"{price/80}" for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)
