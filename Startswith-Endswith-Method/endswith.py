# The endswith() is a string methods that returns True if a specified string ends with a specified value

list1 = ['lemon','Orange', 'apple', 'apricot']

new_list = [i for i in list1 if i.endswith('e')]

print(new_list)

# Output:

['Orange', 'apple']