list1 = ['Mary','Peter', 'Kelly']

a = lambda x: x[-1]

y = sorted(list1, key=a)
print(y)

# Output:
['Peter', 'Mary', 'Kelly']
