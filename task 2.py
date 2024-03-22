import random
import os
import psutil
from memory_profiler import profile

MAX_ORDERS = 100  # Maximum orders allowed

# Function to load orders from a text file
def load_orders_from_file(filename):
    try:
        with open(filename, "r") as file:
            orders = {}
            for line in file:
                orderid, items = line.strip().split(":")
                orders[int(orderid)] = items.split(",")
    except FileNotFoundError:
        orders = {}
    return orders

# Function to save orders to a text file
def save_orders_to_file(filename, orders):
    with open(filename, "w") as file:
        for orderid, items in orders.items():
            file.write(f"{orderid}: {', '.join(items)}\n")

    print(f"Orders saved to: {os.path.abspath(filename)}")

@profile
# Function to add an order
def order_add(firstaid, orders):
    if len(orders) >= MAX_ORDERS:
        print("Maximum orders reached. Cannot add more orders.")
        return

    order = []  # Create an empty list to store the order items
    orderid = random.randint(0, 5000)  # Generate a random order ID
    print("Order ID:", orderid)
    
    while len(order) < 1:  # Allowing a maximum of 5 items per order
        product_code = input("Enter the product code (e.g., 1001) or 'done' to finish: ")
        if product_code == "done":
            break
        if product_code in firstaid:
            quantity = int(input("Enter the quantity: "))
            product_name = firstaid[product_code]
            order.extend([product_name] * quantity)  # Add multiple items based on quantity
            print(f"Added {quantity} {product_name}(s) to the order.")
        else:
            print("Invalid product code. Please try again.")

    orders[orderid] = order  # Add the order to the orders dictionary

@profile
# Function to delete an order
def delete_order(orders):
    orderid = int(input("Enter the order ID to delete: "))
    if orderid in orders:
        del orders[orderid]
        print(f"Order with ID {orderid} deleted successfully.")
    else:
        print("Order ID not found.")

@profile
# Function to modify an order
def modify_order(orders, firstaid):
    orderid = int(input("Enter the order ID to modify: "))
    if orderid in orders:
        print("Current order:")
        for item in orders[orderid]:
            print(item)  # Print each item on a different line
        new_order = []  # Create a new order to replace the existing one
        count = 0  # Initialize count of items added
        while count < 1:  # Allowing a maximum of 5 items per order
            product_code = input("Enter the new product code (e.g., 1001) or 'done' to finish: ")
            if product_code == "done":
                break
            if product_code in firstaid:
                quantity = int(input("Enter the quantity: "))
                product_name = firstaid[product_code]
                new_order.extend([product_name] * quantity)  # Add multiple items based on quantity
                count += quantity
                print(f"Added {quantity} {product_name}(s) to the order.")
            else:
                print("Invalid product code. Please try again.")
        orders[orderid] = new_order  # Update the order in the orders dictionary
        print("Order modified successfully.")
    else:
        print("Order ID not found.")

# Main part of the code
filename = "orders.txt"  # Specify the filename for storing orders
firstaid = {  # Define the first aid items with their corresponding codes
    "1001": "plasters , Sterile Gauze Pads , Adhesive Tape\n",
    "1002": "Antiseptic Wipes , Antibiotic Ointment, Scissors\n\n",
    "1003": "Adhesive Tape, Antiseptic Wipes, Scissors\n\n",
    "1004": "Antiseptic Wipes, Instant Cold Packs, Emergency Blanket\n\n",
    "1005": "Antibiotic Ointment, First Aid Manual, Sterile Eyewash Solution\n"
}
orders = load_orders_from_file(filename)  # Load orders from the file

while True:
    print("---------------------")
    print("---------------------")
    print("------  Menu  -------")
    print("---------------------")
    print("---------------------")
    print("")
    print("")
    print("Pick what you would like to do?:")
    print("1 is make an order")
    print("2 is modify your order")
    print("3 is to delete your order")
    print("4 is to exit")
    option = int(input("Choose an option: "))

    # Perform operations (add, delete, modify, exit)
    if option == 1:  
        print("First Aid Items:")
        for code, items in firstaid.items():
            print(f"Product Code: {code}")
            print(items)
            print("")  # Add an empty line between items
        print("")
        order_add(firstaid, orders)
    elif option == 2:
        print("First Aid Items:")
        for code, items in firstaid.items():
            print(f"Product Code: {code}")
            print(items)
            print("")  # Add an empty line between items
        print("")
        modify_order(orders, firstaid)
    elif option == 3:
        delete_order(orders)
    elif option == 4:
        break
    else:
        print("Invalid option. Please choose again.")

# Save the updated orders to the file
save_orders_to_file(filename, orders)
