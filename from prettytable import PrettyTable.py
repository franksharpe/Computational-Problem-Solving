from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["city", "size"]

table.add_row(["batman", "2000"])

print(table)