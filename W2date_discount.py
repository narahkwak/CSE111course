from datetime import datetime

#dates
current = datetime.now()
weekday = current.isoweekday()

# Inputs

cart_items = float(input("How much is the subtotal? "))
sales_tax = .06 * cart_items

#discount

if weekday ==2 or weekday == 3:
    if cart_items > 50:
        #offer coupon
        new_cart_items = cart_items * .9
        sales_tax = .06 * new_cart_items
        cart_total = new_cart_items + sales_tax
        print(f"sales_tax: {sales_tax:.2f}")
        print(f"Your discounted price is {cart_total:.2f}")
    else: 
        #no coupon
        cart_total = cart_items + sales_tax
        print(f"sales tax: {sales_tax:.2f}")
        print(f"Your total is {cart_total:2f}")
        x = 50 - cart_total 
        print(f"If you buy ${x:.2f} amount more of things you can get you get 10% discount")
else:
    cart_total = cart_items + sales_tax
    print(f"sales tax: {sales_tax:.2f}")
    print(f"Your total is {cart_total:.2f}")
