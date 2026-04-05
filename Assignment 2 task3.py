orders = []

while True:
    print("\n--- MENU ---")
    print("1 — Add order amount")
    print("2 — Show all orders with discount")
    print("q — Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            amount = float(input("Enter order amount: "))
            orders.append(amount)
            print("Order added successfully!")
        except:
            print("Invalid amount! Try again.")
            continue   # re-show menu

    elif choice == '2':
        if not orders:
            print("No orders available.")
            continue

        total = 0
        print("\nOrders after discount:")

        for order in orders:
            if order >= 2000:
                discount = 0.15
            elif order >= 1000:
                discount = 0.10
            else:
                discount = 0.05

            final_price = order - (order * discount)
            total += final_price

            print(f"Original: {order} → After Discount: {final_price}")

        print("Total after discount:", total)

    elif choice == 'q':
        print("Exiting program...")
        break   # exit loop

    else:
        print("Invalid choice! Try again.")
        continue   # re-show menu