# Using the enumerate(), max() functions we can find the index of the biggest number in a list

# First we declare a list with numbers 
x = [23, 56, 90, 76, 72, 89, 456, 43]

# We now use the max num function to get the biggest number in the list
max_num = max(enumerate(x), key = lambda x: x[1])

# We now print out the maximum number in the list
print("The index of the biggest number is", max_num[0] + ", with the actual number being", x.max())

# Output
The index of the biggest guy is 6