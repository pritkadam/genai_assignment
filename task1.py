products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"]
sample_product = ("Smartphone", 10000, "Electronics")

print("Products List:", products[2],products[4])

products.append("Camera")
products.append("Printer")
print("Updated Products List:", products)


# Convert tuple to list
product_list = list(sample_product)
print("Tuple converted to list:", product_list)

# Update the value (e.g., change price from 10000 to 12000)
product_list[1] = 12000
print("Updated list:", product_list)

# Convert back to tuple
updated_product = tuple(product_list)
print("List converted back to tuple:", updated_product)


