def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# Prompting the user for input
price = 400
discount_percent = 50

# Calculating and displaying the final price
final_price = calculate_discount(price, discount_percent)
print("The final price after applying the discount is", final_price)

