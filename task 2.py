import random
import os
from memory_profiler import profile

MAX_ORDERS = 100  # Maximum orders allowed

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def modify_item(self, old_item, new_item):
        if old_item in self.items:
            index = self.items.index(old_item)
            self.items[index] = new_item

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print("Items:")
        for item in self.items:
            print(item)


# Function to load orders from a text file
def load_orders_from_file(filename):
    try:
        with open(filename, "r") as file:
            orders = {}
            for line in file:
                orderid, items = line.strip().split(":")
                order_id = int(orderid)
                order_items = items.split(",")
                orders[order_id] = Order(order_id, order_items)
    except FileNotFoundError:
        orders = {}
    return orders

# Function to save orders to a text file
def save_orders_to_file(filename, orders):
    with open(filename, "w") as file:
        for orderid, order in orders.items():
            order_items_with_quantity = {}  # Dictionary to hold items with their quantities
            for item in order.items:
                quantity = order.items.count(item)  # Count occurrences of each item
                order_items_with_quantity[item] = quantity  # Store item with its quantity in dictionary
            items_string = ', '.join([f"{item} ({quantity})" for item, quantity in order_items_with_quantity.items()])
            file.write(f"{order.order_id}: {items_string}\n")
    print(f"Orders saved to: {os.path.abspath(filename)}")


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

    orders[orderid] = Order(orderid, order)  # Add the order to the orders dictionary

# Function to delete an order
def delete_order(orders):
    orderid = int(input("Enter the order ID to delete: "))
    if orderid in orders:
        del orders[orderid]
        print(f"Order with ID {orderid} deleted successfully.")
    else:
        print("Order ID not found.")

# Function to modify an order
def modify_order(orders, firstaid):
    orderid = int(input("Enter the order ID to modify: "))
    if orderid in orders:
        print("Current order:")
        orders[orderid].display_order()
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
        orders[orderid] = Order(orderid, new_order)  # Update the order in the orders dictionary
        print("Order modified successfully.")
    else:
        print("Order ID not found.")


filename = "orders.txt"  # Specify the filename for storing orders
firstaid = {  # Define the first aid items with their corresponding codes
    "1001": "plasters , Sterile Gauze Pads , Adhesive Tape",
    "1002": "Antiseptic Wipes , Antibiotic Ointment, Scissors",
    "1003": "Adhesive Tape, Antiseptic Wipes, Scissors",
    "1004": "Antiseptic Wipes, Instant Cold Packs, Emergency Blanket",
    "1005": "Antibiotic Ointment, First Aid Manual, Sterile Eyewash Solution"
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
