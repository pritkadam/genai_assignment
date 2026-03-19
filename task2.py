#1
categories = ["Laptop", "Smartphone", "Tablet", "Tablet", "Smartwatch", "Laptop"]
categories_set = set(categories)
print("Categories set:", categories_set)

#2 
categories_set.add("Headphones")
categories_set.add("Laptop") # Duplicate
print("Categories set after adding 'Headphones' and a duplicate 'Laptop':", categories_set)

#3
check_category = "Laptop"
exists = check_category in categories_set
print("Does check_category exist in the set?", exists)
