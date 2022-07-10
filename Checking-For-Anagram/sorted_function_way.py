#You can also use the sorted() function to check if two strings are anagrams. 

a = 'lost'
b = 'stol'
if sorted(a)== sorted(b):
print('Anagrams')
else:
print("Not Anagrams")
# Output:
Anagrams