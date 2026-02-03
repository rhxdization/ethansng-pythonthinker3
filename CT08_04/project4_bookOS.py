inventory = {
    "notebook": 2.50,
    "pencil": 0.50,
    "pen": 1.20,
    "ruler": 1.50,
    "eraser": 0.50,
    "writing pad": 2.50,
    "marker": 2.00,
    "glue": 3.00,
    "calculator": 35.00
}
ordered = {

}
wallet = 50

print("Welcome to the Bookshop Ordering System (BOS)!\n")
while True:
    order = input("What would you like to order? (type quit to quit, type items to see items): ")
    if order == "items":
        for i in inventory:
            print(f"{i}: ${inventory[i]}")
            continue
    elif order == "quit":
        if ordered == {}:
            print("order something bro")
            continue
        else:
            break
    elif order in inventory:
        if order not in ordered:
            ordered[order] = 1
        else:
            ordered[order] += 1
        print(f"Added {order} to your order.")
        continue
    elif order == "ordered":
        print(f"{ordered}")
    else:
        print("Sorry, we dont have that.")

totalcost = 0
for i in ordered:
    totalcost += ordered[i] * inventory[i]

print("----- Order Summary -----\n")
for i in ordered:
    print(f"{i} x {ordered[i]}: ${inventory[i] * ordered[i]}")
if totalcost >= 30:
    totalcost -= (totalcost/10)
    print("\nDiscount: 10% (Spend $30 or more)")
    print(f"Total Cost: ${totalcost}")
else:
    print(f"\nTotal Cost: {totalcost}")
print("-------------------------")
yn = input(f"You have ${wallet}, would you like to purchase? (y/n): ").lower()
if yn == "y":
    if wallet >= totalcost:
        wallet -= totalcost
        print(f"Purchase successful! You have ${wallet} left.")
    else:
        print("You dont have enough money.")
else:
    print("Ok")


# suggestions
# instead of using the method you use previously, do the below challenge
# this is to let use get use of the nested dictionary.
## Challenge 1: Track Quantities of Items
# Allow the customer to specify how many of each item they want to buy.​
# Store both the item and quantity in a nested dictionary.​
# - purchases = ​{"Notebook": {"quantity": 2, "cost": 5.00}}​
# Calculate the total cost based on quantities.
            
            
        