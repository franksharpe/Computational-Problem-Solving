import random

firstaid = {
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

orders = {}

def order_add(firstaid):
    global orders
    order = {}  
    orderid = random.randint(0, 5000)  
    print("Order ID:", orderid)
    
    while True:
        product_code = input("Enter the product code (e.g., 1001) or 'done' to finish: ")
        if product_code == "done":
            break
        if product_code in firstaid:
            product_name = firstaid[product_code]
            order[product_code] = product_name
            print(f"Added {product_name} to the order.")

    orders[orderid] = order  

def delete_order():
    global orders
    orderid = input("Enter the order ID to delete: ")
    if orderid in orders:
        del orders[orderid]
        print(f"Order with ID {orderid} deleted successfully.")
    else:
        print("Order ID not found.")

def modify_order():
    global orders
    orderid = input("Enter the order ID to modify: ")
    if orderid in orders:
        print("Current order:", orders[orderid])
        new_order = {}  
        while True:
            product_code = input("Enter the new product code (e.g., 1001) or 'done' to finish: ")
            if product_code == "done":
                break
            if product_code in firstaid:
                product_name = firstaid[product_code]
                new_order[product_code] = product_name
                print(f"Added {product_name} to the order.")
        orders[orderid] = new_order  
        print("Order modified successfully.")
    else:
        print("Order ID not found.")

# Example usage:
order_add(firstaid)
delete_order()
modify_order()
