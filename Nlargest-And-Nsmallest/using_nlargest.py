# Using Nlargest

# Import the heapq module
import heapq

# Declare a list with integer values
results = [12, 34, 67, 98, 90, 68, 55, 54, 64, 35]

# Find the top Five numbers from the list 
max_list = heapq.nlargest(5, results)

#print the numbers to confirm 
print(max_list)

# Output:
[98, 90, 68, 67, 64]
