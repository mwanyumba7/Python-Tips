# Creating the first dictionaries(flowers) with different flowers and their colors
flowers = {"Acacia": "White",
"Aconite": "blue-purple", "African Daisy": "Gold"}

#Creating the second dictionary(presidents) with Kenyan presidents and their year of birth
presidents = {"Jomo Kenyatta": 1893, "Daniel Arap Moi": 1924}

# Merging the two dictionaries
names = {**flowers, **presidents}
print(names)

# Output
{'Acacia': 'White', 'Aconite': 'blue-purple', 'African Daisy': 'Gold', 'Jomo Kenyatta': 1893, 'Daniel Arap Moi': 1924}

