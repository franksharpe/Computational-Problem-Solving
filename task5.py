defective_prob_u = 0.20  # Probability of receiving a defective item from Uzumaki Safety Suppliers
defective_prob_k = 0.10  # Probability of receiving a defective item from Khairan Safety Company
defective_prob_l = 0  # Probability of receiving a defective item from Leaf First-Aid Kits Ltd

# (a) Probability of receiving a defective item from each supplier
prob_defective_u = 0.50 * defective_prob_u  # Probability of receiving a defective item from Uzumaki Safety Suppliers
prob_defective_k = 0.20 * defective_prob_k  # Probability of receiving a defective item from Khairan Safety Company
prob_defective_l = 0.30 * defective_prob_l  # Probability of receiving a defective item from Leaf First-Aid Kits Ltd

total_defective_prob = prob_defective_u + prob_defective_k + prob_defective_l  # Total probability of receiving a defective item
print("Probability of receiving a defective item:", total_defective_prob*100)

# (b) Probability that a defective item came from Uzumaki Safety Suppliers
# Applying Bayes' theorem: P(Uzumaki | Defective) = P(Defective | Uzumaki) * P(Uzumaki) / P(Defective)
prob_defective_from_u = prob_defective_u / total_defective_prob
print("Probability that a defective item came from Uzumaki Safety Suppliers:", prob_defective_from_u*100)

# (c) Discussion
# Compare the total probability of receiving a defective item before and after introducing Leaf First-Aid Kits Ltd
old_total_defective_prob = defective_prob_u + defective_prob_k  # Total probability of receiving a defective item with two suppliers
new_total_defective_prob = total_defective_prob  # Total probability of receiving a defective item with three suppliers

# Assess whether introducing Leaf First-Aid Kits Ltd has helped by comparing the total defective probabilities
if new_total_defective_prob < old_total_defective_prob:
    print("Introducing Leaf First-Aid Kits Ltd has helped.")
elif new_total_defective_prob > old_total_defective_prob:
    print("Introducing Leaf First-Aid Kits Ltd has not helped.")
else:
    print("Introducing Leaf First-Aid Kits Ltd has had no impact.")
