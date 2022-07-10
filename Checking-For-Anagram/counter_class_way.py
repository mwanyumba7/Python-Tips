# If you want to check if two strings are anagrams, you can use the Counter() class from the collections module.

from collections import Counter

a = 'lost'

b = 'stol'
print(Counter(a)==Counter(b))

#Output:
True