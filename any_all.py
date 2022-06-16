# Created on Jun 16, 2022
#
# @author: Jim Yin

# Examples of using any and all functions


x = [True, True, False, True]

print(any(x))

print(all(x))

y = [2, 4, 6, 8, 10]
z = [1, 2, 3, 4, 5]

print(any([i % 2 == 0 for i in z]))
print(all([i % 2 == 0 for i in y]))