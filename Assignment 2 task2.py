orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders = 0

print("Order Amount | Discount % | Final Amount")
print("----------------------------------------")

for order in orders:

    if order >= 2000:
        discount = 0.15
    elif 1500 <= order < 2000:
        discount = 0.10
    elif 1000 <= order < 1500:
        discount = 0.07
    else:
        discount = 0.0

    discount_amount = order * discount
    final_amount = order - discount_amount

    if discount > 0:
        discounted_orders += 1

    total_revenue += final_amount

    print(f"{order} \t | {discount*100}% \t | {final_amount}")

print("Total Revenue after Discounts:", total_revenue)
print("Number of Discounted Orders:", discounted_orders)