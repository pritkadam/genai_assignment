product_list = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"]
price_dict = {
    'Mobile': 20000,
    'Laptop': 15000,
    'Earphones': 2000,
    'Tablet': 10000,
    'Smartwatch': 5000,
    'Headphones': 3000
}


catalog = [
    ("Mobile", price_dict["Mobile"],"Electronics"),
    ("Laptop", price_dict["Laptop"],"Electronics"),
    ("Earphones", price_dict["Earphones"],"Accessories"),
    ("Tablet", price_dict["Tablet"],"Electronics"),
    ("Smartwatch", price_dict["Smartwatch"],"Wearables"),
    ("Headphones", price_dict["Headphones"],"Accessories")
]

print("Catalog of products:",catalog)
print(type(catalog))

#2
category_to_products = {}
for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append((product, price))

print("Products by category:",category_to_products)

max_category = max(category_to_products, key=lambda c: len(category_to_products[c]))
print("Category with the most products:", max_category)

print("Products in the category with the most products:", category_to_products[max_category])