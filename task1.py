import random

# Function to load orders from a text file
def load_orders_from_file(filename):
    try:
        with open(filename, "r") as file:
            # Read lines from the file and split each line into order ID and items
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
            # Write each order as "orderid: item1, item2, item3"
            file.write(f"{orderid}: {', '.join(items)}\n")
            
            
# Function to add an order
def order_add(firstaid, orders):
    order = []  # Create an empty list to store the order items
    orderid = random.randint(0, 5000)  # Generate a random order ID
    print("Order ID:", orderid)
    
    while len(order) < 5:  # Allowing a maximum of 5 items per order
        product_code = input("Enter the product code (e.g., 1001) or 'done' to finish: ")
        if product_code == "done":
            break
        if product_code in firstaid:
            product_name = firstaid[product_code]
            order.append(product_name)
            print(f"Added {product_name} to the order.")
        else:
            print("Invalid product code. Please try again.")

    orders[orderid] = order  # Add the order to the orders dictionary
    
    
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
        print("Current order:", orders[orderid])
        new_order = []  # Create a new order to replace the existing one
        count = 0  # Initialize count of items added
        while count < 5:  # Allowing a maximum of 5 items per order
            product_code = input("Enter the new product code (e.g., 1001) or 'done' to finish: ")
            if product_code == "done":
                break
            if product_code in firstaid:
                product_name = firstaid[product_code]
                new_order.append(product_name)
                count += 1
                print(f"Added {product_name} to the order.")
            else:
                print("Invalid product code. Please try again.")
        orders[orderid] = new_order  # Update the order in the orders dictionary
        print("Order modified successfully.")
    else:
        print("Order ID not found.")


# Main part of the code
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
orders = load_orders_from_file(filename)  # Load orders from the file

# Perform operations (add, delete, modify)
order_add(firstaid, orders)
modify_order(orders)
delete_order(orders)
# Save the updated orders to the file
save_orders_to_file(filename, orders)
