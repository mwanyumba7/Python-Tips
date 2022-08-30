# 1. Using set comprehension

dict1 = {'name': 'Mary', 'age': 22,

'student':True,'Country': 'UAE'}
print({i for i in dict1.keys()})
#Output:
{'age', 'student', 'Country', 'name'}
