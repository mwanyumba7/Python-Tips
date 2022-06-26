# We can also use list comprehension to flatten a nested list

# We then declare a list Aloha meaning

alohaMeaning = [["Love", "Peace"], ["Affection", "Compassion"]]

# We now flatten the list 

flat_alohaMeaning = [i for j in alohaMeaning for i in j]

# Lets print and see this changes
print(flat_alohaMeaning)

# Output
['Love', 'Peace', 'Affection', 'Compassion']