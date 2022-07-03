# The startswith() is a string method that return True if a specified string starts with a specified value.

list1 = ['lemon','Orange', 'apple', 'apricot']

new_list = [i for i in list1 if i.startswith('a')]

print(new_list)

# Output:

['apple', 'apricot']
