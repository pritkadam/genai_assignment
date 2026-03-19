# Task 1: Product Collections (Lists & Tuples)

# 1. Create a list named products containing at least 6 product names
products = ["Laptop", "Smartphone", "Headphones", "Monitor", "Keyboard", "Mouse"]
print(f"Initial products: {products}")

# 2. Create a tuple named sample_product
sample_product = ("Laptop", 999.99, "Electronics")
print(f"Sample product tuple: {sample_product}")

# 3. Print the 2nd and last product from the products list
print(f"2nd product: {products[1]}")
print(f"Last product: {products[-1]}")

# 4. Append two new product names and print the updated list
products.append("Webcam")
products.append("Microphone")
print(f"Updated products list: {products}")

# Extra (optional): Modify sample_product tuple
temp_list = list(sample_product)
temp_list[1] = 899.99  # Change price
sample_product = tuple(temp_list)
print(f"Updated sample product tuple: {sample_product}")

print("-" * 30)

# Task 2: Categories (Sets)

# 1. Create a set of categories called categories_set
# Since products don't contain categories, we'll use a parallel list as suggested
categories = ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories", "Accessories", "Peripherals", "Peripherals"]
categories_set = set(categories)
print(f"Initial categories set: {categories_set}")

# 2. Demonstrate adding a new category and ignoring duplicates
categories_set.add("Storage")
categories_set.add("Electronics") # Duplicate
print(f"Categories set after adding 'Storage' and a duplicate 'Electronics': {categories_set}")

# 3. Check whether a category exists in the set
check_category = "Electronics"
exists = check_category in categories_set
print(f"Does '{check_category}' exist in the set? {exists}")

# Extra (optional): Get the total number of unique categories
total_unique = len(categories_set)
print(f"Total number of unique categories: {total_unique}")
