#This is how you can use code to check if an item is iterable or not. We are using the iter() function'''

a = ['i','love','working', 'with', 'Python']

try:

iter_check = iter(a)
except TypeError:
print('Object a not iterable')
else:
print('Object a is iterable')
# Check the second object
b = 45.7
try:
iter_check = iter(b)
except TypeError:
print('Object b is not iterable')
else:
print('Object b is iterable')
