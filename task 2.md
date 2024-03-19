task 2 


Recreated Algorithm for Tanjiro Safety Products Ltd
Justification of Abstract Data Type (ADT) Selection:
For the scenario of order management at Tanjiro Safety Products Ltd, a suitable ADT is a list of dictionaries in Python. This choice is made considering the need for efficient storage and retrieval of orders while maintaining flexibility in handling order details.

List: Lists provide sequential storage, allowing easy access to orders based on their position in the list. This sequential nature aligns well with the chronological order of placing orders, making it convenient for order management.

Dictionary: Each order is represented as a dictionary within the list, with keys representing order attributes such as order ID and items. Dictionaries offer fast retrieval of order information using unique keys, ensuring efficient order manipulation operations.

python:



Explanation of the Code:

List of Dictionaries: Orders are stored as dictionaries within a list. Each dictionary represents an order, with keys "orderid" and "items".
order_add: Prompts the user to create a new order and appends it to the orders list.
delete_order: Deletes an existing order from the orders list based on the provided order ID.
modify_order: Allows the user to modify an existing order by updating its items.

Time Complexity (Big O Notation):

order_add: O(n), where n is the number of items in the order.

delete_order: O(n), as it may need to iterate through the entire list to find the order to delete.

modify_order: O(n), as it may need to iterate through the entire list to find the order to modify.

Overall, this algorithm offers efficient order management for Tanjiro Safety Products Ltd, ensuring smooth operations and customer satisfaction.

