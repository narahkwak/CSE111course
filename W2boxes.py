import math

items = int(input("Enter the number of items: "))
items_box = int(input("Enter the number of items per box: "))

calculation = float(items / items_box)
rounding = math.ceil(calculation)

print(f"For {items}, packing {items_box} items in each box, you will need {rounding} boxes.")