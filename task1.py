# libarys 

import random
import os
import psutil
from memory_profiler import profile

MAX_ORDERS = 20  # Maximum orders allowed

# Function to load orders from a text file
def load_orders_from_file(filename):
    try:
        # Open the file for reading
        with open(filename, "r") as file:
            orders = {}  # Initialize an empty dictionary to store orders
            # Iterate through each line in the file
            for line in file:
                # Split each line into orderid and items
                orderid, items = line.strip().split(":")
                # Convert orderid to integer and split items into a list
                orders[int(orderid)] = items.split(",")
    except FileNotFoundError:
        # If the file is not found, return an empty dictionary
        orders = {}
    # Return the dictionary containing the loaded orders
    return orders


# Function to save orders to a text file
def save_orders_to_file(filename, orders):
    with open(filename, "w") as file: # open file as write
        for orderid, items in orders.items():
            file.write(f"{orderid}: {', '.join(items)}\n") # write orders in file each on new line

    print(f"Orders saved to: {os.path.abspath(filename)}") # shows where saved to
    print(f"Maximum orders allowed: {MAX_ORDERS}") # show max orders 

@profile
# Function to add an order 
def order_add(firstaid, orders):
    
    order = []  # Create an empty list to store the order items
    orderid = random.randint(0, 5000)  # Generate a random order ID from 0 to 5000
    print("Order ID:", orderid)
    
    while len(order) < 5:  # Allowing a maximum of 5 items per order
        product_code = input("Enter the product code (e.g., 1001) or 'done' to finish: ")
        if product_code == "done":
            break   # Ends the code if "done" is selected 
        if product_code in firstaid:
            quantity = int(input("Enter the quantity: ")) 
            product_name = firstaid[product_code]
            order.extend([product_name] * quantity)  # Add multiple items based on quantity
            print(f"Added {quantity} {product_name}(s) to the order.")
        else:
            print("Invalid product code. Please try again.")

    orders[orderid] = order  # Add the order to the orders dictionary , once ended saved to the file
   

@profile
# Function to delete an order
def delete_order(orders):
   
    orderid = int(input("Enter the order ID to delete: ")) # takes the user input
    if orderid in orders:  # Checks if the order id is in orders
        del orders[orderid]
        print(f"Order with ID {orderid} deleted successfully.") # output msg
    else:
        print("Order ID not found.") # error message
   

@profile
# Function to modify an order
def modify_order(orders, firstaid):
    
    orderid = int(input("Enter the order ID to modify: ")) # gets user input
    if orderid in orders: # checks if order id is in file
        print("Current order:", orders[orderid])
        new_order = []  # Create a new order to replace the existing one
        count = 0  # count of items added starts at 0
        while count < 5:  # Allowing a maximum of 5 items per order
            product_code = input("Enter the new product code (e.g., 1001) or 'done' to finish: ")
            if product_code == "done":
                break
            if product_code in firstaid: # checks the input aligns up
                quantity = int(input("Enter the quantity: "))
                product_name = firstaid[product_code]
                new_order.extend([product_name] * quantity)  # Add multiple items based on quantity
                count += quantity
                print(f"Added {quantity} {product_name}(s) to the order.") # output message
            else:
                print("Invalid product code. Please try again.")
        orders[orderid] = new_order  # Update the order in the orders dictionary
        print("Order modified successfully.")
    else:
        print("Order ID not found.")
    

filename = "orders.txt"  # Specify the filename for storing orders
firstaid = {  # Define the first aid items with their corresponding codes
    "1001": "plasters",
    "1002": "Sterile Gauze Pads",
    "1003": "Adhesive Tape",
    "1004": "Antiseptic Wipes",
    "1005": "Antibiotic Ointment",
    "1006": "Scissors",
    "1007": "Tweezers",
    "1008": "Disposable Gloves",
    "1009": "Instant Cold Packs",
    "1010": "CPR Mask",
    "1011": "Emergency Blanket",
    "1012": "Sterile Eyewash Solution",
    "1013": "Burn Cream",
    "1014": "First Aid Manual"
}
# Update the firstaid dictionary to print each item on a new line
firstaid = {code: f"{code}: {item}\n" for code, item in firstaid.items()}

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
        for item in firstaid.values():
            print(item)  # Print each item on a new line
        print("")
        order_add(firstaid, orders)
    elif option == 2:
        print("First Aid Items:")
        for item in firstaid.values():
            print(item)  # Print each item on a new line
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
