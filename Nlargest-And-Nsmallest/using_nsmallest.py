#Using Nsmallest

# Import the headq module 
Import headq

#Declare a non-empty list with integers
Results =[12, 34, 67, 98, 90, 68, 55, 54, 64, 35]

# Find the 5 smallest numbers from the list
min_list = heapq.nsmallest(5, results)

# Print the numbers to confirm 
print(min_list)

#Output:

[12, 34, 35, 54, 55]