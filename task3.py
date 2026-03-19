#1
price_dict = {
    'Mobile': 20000,
    'Laptop': 15000,
    'Earphones': 2000,
    'Tablet': 10000,
    'Smartwatch': 5000,
    'Headphones': 3000
}
#2
price_dict['Camera'] = 12000

price_dict.update(Mobile=18000)

price_dict.pop('Tablet')
print(price_dict)

#3

total_price = sum(price_dict.values())
count = len(price_dict)

average_price = total_price / count

print("Average price of all items:", average_price)