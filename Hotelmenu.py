menu = {
    "Pizza" : 100,
    "Burger" : 55,
    "Past" : 70,
    "Momos" : 80,
    "Coffee" : 50
}
print("Welcome to PYTHON Restaurant \n")

for items in menu:
    print(f"{items} - ₹{menu[items]}")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu :
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else :
    print(f"Ordered item {item_1} is not available yet")


another_item = input("Do you want to add another item? (Yes/No)")
if another_item == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else :
        print(f"Ordered item {item_2} is not available")

print(f"The total amount of items to pay is {order_total} ")