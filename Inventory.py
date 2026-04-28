def get_price_category(price):
    if price < 50:
        return "Budget"
    elif price < 200:
        return "Mid-range"
    else:
        return "Premium"


def check_stock_level(stock):
    if stock >= 10:
        return "OK"
    else:
        return "LOW STOCK - Reorder needed"


def save_product(name, price, category, stock, stock_status):
    with open(r'C:\Users\USER\OneDrive\Desktop\Inventory.txt', "a") as file:
        file.write(f"Product: {name} | Price: P{price:.2f} | Category: {category} | Stock: {stock} | Status: {stock_status}\n")


while True:
    name = input("Enter product name: ")
    price = float(input("Enter price: (in pesos) "))
    stock = int(input("Enter stock quantity: "))

    category = get_price_category(price)
    stock_status = check_stock_level(stock)

    print("\n--- PRODUCT INFO ---")
    print(f"Name: {name}")
    print(f"Price: P{price:.2f}")
    print(f"Category: {category}")
    print(f"Stock: {stock}")
    print(f"Stock Status: {stock_status}")

    save_product(name, price, category, stock, stock_status)
    print("Product saved to inventory.txt\n")

    choice = input("Add another product? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting program...")
        break