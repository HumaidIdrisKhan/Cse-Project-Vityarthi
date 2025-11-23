import random
import datetime
from collections import Counter
# LOGIN SYSTEM
def login():
    print("\n=== LOGIN ===")
    username = input("Enter your name: ")
    print(f"Welcome, {username}!\n")
    return username
# 30 ITEM PRODUCT DATABASE (price, stock)
products = {
    "Rice 1kg": [60, 20], "Wheat Flour 1kg": [45, 18], "Sugar 1kg": [50, 25],
    "Milk 1L": [55, 22], "Eggs 6pc": [40, 30], "Bread": [30, 15],
    "Butter 200g": [48, 10], "Cheese 200g": [75, 9], "Tea 250g": [110, 10],
    "Coffee 200g": [150, 8], "Salt 1kg": [20, 40], "Oil 1L": [135, 17],
    "Soap": [35, 25], "Shampoo 200ml": [95, 12], "Toothpaste": [60, 20],
    "Pen": [10, 50], "Notebook": [40, 28], "Pencil": [5, 60],
    "Eraser": [3, 40], "Sharpener": [7, 35], "Water Bottle": [90, 10],
    "Chips": [20, 30], "Chocolate": [25, 25], "Biscuits": [15, 40],
    "Noodles": [12, 33], "Ketchup": [85, 12], "Jam": [75, 10],
    "Maggie Pack": [14, 36], "Detergent 1kg": [95, 14], "Tissue Pack": [35, 20]
}
# SHOPPING CART STORAGE
cart_items = []          # stores item names
cart_prices = []         # stores prices
# DISPLAY ITEMS
def display_items():
    print("\n=== AVAILABLE ITEMS (Price | Stock) ===")
    for item, info in products.items():
        print(f"{item} - ₹{info[0]} | Stock: {info[1]}")
    print()
# ADD TO CART
def add_to_cart():
    display_items()
    item = input("Enter item to add: ")
    if item not in products:
        print("❌ Item does not exist.\n")
        return
    quantity = int(input("Enter quantity: "))
    if quantity > products[item][1]:
        print("❌ Not enough stock!\n")
        return
    # Deduct stock & add multiple items to cart
    products[item][1] -= quantity
    for _ in range(quantity):
        cart_items.append(item)
        cart_prices.append(products[item][0])
    print(f"✔ Added {quantity} x {item} to cart.\n")
# REMOVE MULTIPLE ITEMS AT ONCE
def remove_from_cart():
    if not cart_items:
        print("❌ Cart is empty!\n")
        return
    print("\nYour Cart Items:")
    item_counts = Counter(cart_items)
    for itm, qty in item_counts.items():
        print(f"{itm} x {qty}")
    item = input("\nEnter item to remove: ")
    if item not in cart_items:
        print("❌ That item is not in the cart.\n")
        return
    max_qty = cart_items.count(item)
    qty_remove = int(input(f"Enter quantity to remove (max {max_qty}): "))
    if qty_remove > max_qty:
        print("❌ You don't have that many in your cart.\n")
        return
    # Remove from cart and restore stock
    for _ in range(qty_remove):
        cart_items.remove(item)
        cart_prices.remove(products[item][0])
        products[item][1] += 1
    print(f"✔ Removed {qty_remove} x {item} from cart.\n")
# APPLY COUPON
def apply_coupon(total):
    code = input("\nEnter coupon code (SAVE10): ")
    if code == "SAVE10":
        print("✔ Coupon applied: 10% OFF!")
        return total * 0.90
    else:
        print("❌ Invalid coupon.")
        return total
# CHECKOUT (with frequency table)
def checkout(username):
    if not cart_items:
        print("❌ Cart is empty!\n")
        return
    print("\n=== CHECKOUT SUMMARY ===")
    item_counts = Counter(cart_items)
    total = 0
    print("\nItem                     Qty     Unit Price     Subtotal")
    print("-------------------------------------------------------------")
    for item, qty in item_counts.items():
        price = products[item][0]
        sub_total = price * qty
        total += sub_total
        print(f"{item:20}  {qty:<5}   {price:<12}   {sub_total}")
    print("\nTotal Amount:", total)
    total = apply_coupon(total)
    print(f"Final Payable: ₹{total:.2f}")
    address = input("\nEnter delivery address: ")
    order_id = random.randint(10000, 99999)
    delivery_days = random.randint(3, 7)
    delivery_date = datetime.date.today() + datetime.timedelta(days=delivery_days)
    print("\n✔ ORDER CONFIRMED!")
    print(f"Order ID: {order_id}")
    print(f"Estimated Delivery: {delivery_date}")
    print("Receipt saved as receipt.txt\n")
    save_receipt(username, order_id, address, item_counts, total, delivery_date)
    cart_items.clear()
    cart_prices.clear()
# SAVE RECEIPT (frequency table)
def save_receipt(username, order_id, address, item_counts, total, delivery_date):
    try:
        with open("receipt.txt", "w", encoding="utf-8") as f:
            f.write("===== RECEIPT =====\n")
            f.write(f"Customer: {username}\n")
            f.write(f"Order ID: {order_id}\n\n")
            f.write("Item                     Qty     Unit Price     Subtotal\n")
            f.write("-------------------------------------------------------------\n")
            for item, qty in item_counts.items():
                price = products[item][0]
                subtotal = qty * price
                f.write(f"{item:20}  {qty:<5}   {price:<12}   {subtotal}\n")
            f.write(f"\nFinal Amount: ₹{total}\n")
            f.write(f"Delivery Address: {address}\n")
            f.write(f"Estimated Delivery: {delivery_date}\n")
            f.write("====================\n")
        print("✔ Receipt saved successfully.\n")
    except Exception as e:
        print("⚠ ERROR writing receipt:", e)
# MAIN LOOP
username = login()
while True:
    print("=== MENU ===")
    print("1. View Items")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. Checkout")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        display_items()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        remove_from_cart()
    elif choice == "4":
        checkout(username)
    elif choice == "5":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice.\n")
