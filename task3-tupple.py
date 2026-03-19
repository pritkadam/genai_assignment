
# Task 2: Categories (Sets)

# 1. Create a set of categories called categories_set
# Since products don't contain categories, we'll use a parallel list as suggested
categories = ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories", "Accessories", "Peripherals", "Peripherals"]
categories_set = set(categories)
print("Initial categories set:", (categories_set))

# 2. Demonstrate adding a new category and ignoring duplicates
categories_set.add("Storage")
categories_set.add("Electronics") # Duplicate
print("Categories set after adding 'Storage' and a duplicate 'Electronics':" ,(categories_set))

# 3. Check whether a category exists in the set
check_category = "Electronics"
exists = check_category in categories_set
print("Does '{check_category}' exist in the set? ",(exists))

# Extra (optional): Get the total number of unique categories
total_unique = len(categories_set)
print("Total number of unique categories: ",(total_unique))
