def parādīt_preces(products, prices):
    print("\nAvailable products:")
    for i in range(len(products)):
        print(f"{products[i]} - €{prices:2f}")
def ievietot_grozā(products, prices):
    cart_products = []
    cart_prices = []
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
    return cart_products, cart_prices
def parādīt_grozu(cart_products, cart_prices):
    print("\n=== YOUR CART ===")
    for i in range(len(cart_products)):
        print(f"{i + 1}. {cart_products[i]} - €{cart_prices:.2f}")
def aprēķināt_cenu(cart_prices):
    total = 0
    for price in cart_prices:
        total = total + price
    return total
def aprēķina_cenu(total):
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
    return discount, final_price
def maksājums(final_price):
    payment = float(input("\nEnter payment amount: €"))
    while payment < final_price:
        print("Not enough money!")

        missing = final_price - payment
        print(f"You are missing €{missing:.2f}")
        payment = float(input("Enter payment amount: €"))
    return payment
def izvadīt_informāciju(cart_products, cart_prices, total, discount, payment, change):
    print("\n=== RECEIPT ===")
    for i in range(len(cart_products)):
        print(f"{cart_products[i]} - €{cart_prices:.2f}")
    print(f"\nTotal: €{total:.2f}")
    print(f"Discount: €{discount:.2f}")
    print(f"Paid: €{payment:.2f}")
    print(f"Change: €{change:.2f}")
def izņemt_produktu(cart_products :list, cart_prices):
    ievade = int(input("Enter the number of the item you wish to remove: ")) - 1
    if ievade < len(cart_products):
        cart_products.pop(ievade)
        cart_prices.pop(ievade)
    return cart_products, cart_prices

products = ["apple", "bread", "milk", "cheese"]
prices = [0.80, 1.50, 1.20, 3.50]
parādīt_preces(products, prices)

cart_products, cart_prices = ievietot_grozā(products, prices)
parādīt_grozu(cart_products, cart_prices)

# Uzdevums: Uzrakstīt funkciju, kas izņem produktu no groza
cart_products, cart_prices = izņemt_produktu(cart_products, cart_prices)
parādīt_grozu(cart_products, cart_prices)

total = aprēķināt_cenu(cart_prices)
print(f"Total: €{total:.2f}")

discount, final_price = aprēķina_cenu(total)
print(f"Discount: €{discount:.2f}")
print(f"Final price: €{final_price:.2f}")

payment = maksājums(final_price)
change = payment - final_price

izvadīt_informāciju(cart_products, cart_prices, total, discount, payment, change)
print("\nThank you for shopping!")