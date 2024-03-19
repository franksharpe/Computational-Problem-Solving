defective_prob_u = 0.20  # Probability of receiving a defective item from Uzumaki Safety Suppliers
defective_prob_k = 0.10  # Probability of receiving a defective item from Khairan Safety Company
uzumaki_kits = 1500  # Number of kits supplied annually by Uzumaki Safety Suppliers
khairan_kits = 500   # Number of kits supplied annually by Khairan Safety Company

# (a) Probability of receiving a defective item
total_kits = uzumaki_kits + khairan_kits  # Total number of kits supplied annually
total_defective = (uzumaki_kits * defective_prob_u) + (khairan_kits * defective_prob_k)  # Total number of defective kits
prob_defective = total_defective / total_kits  # Probability of receiving a defective item
print("Probability of receiving a defective item:", prob_defective*100)

# (b) Probability that a defective item came from Uzumaki Safety Suppliers
prob_defective_u = (uzumaki_kits * defective_prob_u) / total_defective *100  # Probability that a defective item came from Uzumaki Safety Suppliers
print("Probability that a defective item came from Uzumaki Safety Suppliers:", prob_defective_u)
