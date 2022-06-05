'''
Created on Jun 5, 2022

@author: Jim Yin
'''

'''
Iterate with enumerate instead of rane(len(x))
'''

data = [1, 2, -4, -3]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0
        
print(data)

for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0
              
print(data)


'''
Use list comprehension instead of raw for loops
'''

squares = []
for i in range(10):
    squares.append(i**2)
    
print(squares)

squares = [i**2 for i in range(10)]

print(squares)

'''
Sort complex iterables with sorted()
'''

data = [3, 1, 2, 7, 4]
sorted_data = sorted(data, reverse=True)

print(sorted_data)

data = [{'name': 'Max', 'age':6},
        {'name': 'Lisa', 'age':20},
        {'name': 'Ben', 'age':9}]

sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)

'''
Store unique values with Set
'''


'''
Save memory with generators
'''

'''
Define default values in Dictionaries with .get() and .setdefault()
'''

my_dict = {'item': 'football', 'price': 10.00}
count = my_dict.get('count', 0)
print(count)
print(my_dict)

count = my_dict.setdefault('count', 0)
print(count)
print(my_dict)

'''
Count hashable objects with collections.Counter
'''

from collections import Counter

my_list = [10, 10, 10, 4, 3, 4, 5, 9, 9, 9, 9, 9]
counter = Counter(my_list)

print(counter)
print(counter[10])
print(counter[11])

most_common = counter.most_common(1)
print(most_common[0][0])

'''
Format Strings with f-strings
'''

'''
Concatenate strings with .join()
'''

