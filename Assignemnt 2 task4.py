daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for day in daily:
    
    if day == -1:
        print("Corrupted data found! Stopping process.")
        break   # stop loop
    
    if day == 0:
        print("No sales today. Skipping...")
        continue   # skip this iteration
    
    total_sales += day
    print("Running total:", total_sales)

print("Final total sales:", total_sales)