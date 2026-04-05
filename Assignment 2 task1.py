try:
    order_amount = float(input("Enter the order amount: "))

    if order_amount >= 2000:
        discount = 0.15
    elif 1500 <= order_amount < 2000:
        discount = 0.10
    elif 1000 <= order_amount < 1500:
        discount = 0.07
    else:
        discount = 0.0

    discount_amount = order_amount * discount
    subtotal = order_amount - discount_amount

    # Extra: Add 5% tax
    tax = subtotal * 0.05
    final_amount = subtotal + tax

    print("\n--- Bill Summary ---")
    print("Original Amount:", order_amount)
    print("Discount Applied:", discount * 100, "%")
    print("Subtotal after Discount:", subtotal)
    print("Tax (5%):", tax)
    print("Final Amount:", final_amount)

except ValueError:
    print(" Error: Please enter a valid numeric value.")