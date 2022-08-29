import sys
a = ['Love', 'Cold', 'Hot', 'Python']
b = {'Love', 'Cold', 'Hot', 'Python'}
print(f'The memory size of a list is '
f'{sys.getsizeof(a)} ')
print(f'The memory size of a set is '
f'{sys.getsizeof(b)} ')
Output:
The memory size of a list is 120 
The memory size of a set is 216