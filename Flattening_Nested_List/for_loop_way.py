# We can flatten a nested list in three ways , one being using a for loop

# First we declare a nested list
missWorld = [["Tasha", "Rames", "Rexina"], ["Wendy","Amara", "Benta"]]

# We then create a new list that will store our new lst
newList = []
# Then we declare a foor loop
for name in missWorld:
	for j in name:
		newList.append(j)

# We now print the list to see the change
print(newList)

# Output
['Tasha', 'Rames', 'Rexina', 'Wendy', 'Amara', 'Benta']