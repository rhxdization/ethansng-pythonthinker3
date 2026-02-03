menu = {
    "cheeseburger": 5,
    "chicken burger": 6,
    "spicy chicken burger": 7,
    "veggie burger": 5,
    "fries": 2,
    "nuggets": 4,
    "soda": 1,
    "salad": 3
}
order = {

}

# need to write the code here for the task 1: suggested output below
# Welcome to HanBaoBao!

# Here’s our menu: 
# Cheeseburger: $5.50 
# Fries: $3.00 
# Coke: $2.00 
# Ice Cream: $4.00 
# Nuggets: $6.00


money = 20
totalcost = 0

while input != "quit":
    item = input("What would you like to order? (type 'quit' to finish, type menu for menu) ").lower()
    if item == "quit":
        if order == {}:
            print("order something bro 😭")
            continue
        else:
            break
    if item == "menu":
        for i in menu:
            print(f"{i}: ${menu[i]}")
        continue
    if item in menu:
        if item in order:
            order[item] += 1
        else:
            order[item] = 1
        print(f"Added {item} to your order.")
    else:
        print(f"Sorry, we don't have {item} on the menu.")

for i in order:
    item_cost = menu[i] * order[i]
    totalcost += item_cost
print("---- Order Summary ---- ")
# this is good showing the quantity and order
for i in order:
    print(f" {i} x {order[i]}: ${menu[i] * order[i]}")
print(f"----------------------- \n Total Cost: ${totalcost}")
input = input("Would you like to purchase? (y/n): ").lower()
if input == "y":
    if totalcost <= money:
        money -= totalcost
        print(f"Purchase successful! You have ${money} left.")
    else:
        print("Sorry, you do not have enough money for this purchase.")

# --- Order Summary ---
# Fries:          $3.00
# Burger:         $5.00
# Apple Pie:      $2.50

# ---------------------
# Total:         $10.50

# Your total bill is $10.50. Enjoy your meal!
# https://www.w3schools.com/python/python_string_formatting.asp

# how about doing one more challenge which let customer remove items
# this is to practice the delete entry from dictionary
# suggested output
# What would you like to order? remove Fries
# Fries has been removed from your order.

# What would you like to order? remove Burger
# Burger is not in your order.

