# Using enumerate and min() we can also find the index of the smallest number of the list

# Now we will creat a list where the user will input values
y = [9, 500, 800, 89, 94, 90, 56, 74, 29]

# Find the smallest value in the list
min_num = min(enumerate(x), key = lambda x: x[1])

# Print out the index of the smallest num
print("The index of the smallest num is", min_num[0]) 

# Output
The index of the smallest num is 0