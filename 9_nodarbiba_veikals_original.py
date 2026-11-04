products = ["apple", "bread", "milk", "cheese"]
prices = [0.80, 1.50, 1.20, 3.50]

cart_products = []
cart_prices = []

print("\nAvailable products:")

for i in range(len(products)):
    print(f"{products[i]} - €{prices:2f}")


while True:
    product = input("\nEnter product (or 'done' to finish): ").lower()

    if product == "done":
        break

    if product not in products:
        print("Product not found!")
        continue

    index = products.index(product)
    price = prices[index]

    cart_products.append(product)
    cart_prices.append(price)

    print(f"Added {product} - €{price:.2f}")


print("\n=== YOUR CART ===")

for i in range(len(cart_products)):
    print(f"{i + 1}. {cart_products[i]} - €{cart_prices:.2f}")


total = 0

for price in cart_prices:
    total = total + price

print(f"\nTotal: €{total:.2f}")


if total >= 20:
    discount = total * 0.10
    print("You receive a 10% discount!")
elif total >= 10:
    discount = total * 0.05
    print("You receive a 5% discount!")
else:
    discount = 0
    print("No discount.")

final_price = total - discount

print(f"Discount: €{discount:.2f}")
print(f"Final price: €{final_price:.2f}")


payment = float(input("\nEnter payment amount: €"))

while payment < final_price:
    print("Not enough money!")

    missing = final_price - payment
    print(f"You are missing €{missing:.2f}")

    payment = float(input("Enter payment amount: €"))


change = payment - final_price

print("\n=== RECEIPT ===")

for i in range(len(cart_products)):
    print(f"{cart_products[i]} - €{cart_prices:.2f}")

print(f"\nTotal: €{total:.2f}")
print(f"Discount: €{discount:.2f}")
print(f"Paid: €{payment:.2f}")
print(f"Change: €{change:.2f}")

print("\nThank you for shopping!")