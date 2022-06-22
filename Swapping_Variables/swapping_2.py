# We can also swap variables using XOR^ this is a three step methiod

# We first declare the variables
x = 40
y = 67

# Step one 
x ^= y 

# Step two
y ^= x

# Step three
x ^= y

# Print out x and y to see the changes
print(f"x is: {x}")
print(f"y is: {y}")

# Output
x is: 67
y is: 40