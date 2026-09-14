# the two typical attributes of set: Disorderliness and Anisotropy
# {} isnt an empty set but a empty dictionary.
set1 = {1, 2, 3, 3, 3, 2}  # {1, 2, 3}
set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}  # {'pitaya', 'banana', 'grape', 'apple'}
set3 = set('hello')  # {'o', 'l', 'e', 'h'}
set4 = set([1, 2, 2, 3, 3, 3, 2, 1])  # {1, 2, 3}
set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}  # {3, 6, 7, 9, 12, 14, 15, 18}
# The elements in the set must be hashable(int, float, bool, str, tuple).
set0 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
for elem in set1:
    print(elem)
# The export of instance demonstrates the Anisotropy of the set.

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}
print(set1 & set2)                      # {2, 4, 6}
print(set1.intersection(set2))          # {2, 4, 6}
print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1 - set2)                      # {1, 3, 5, 7}
print(set1.difference(set2))            # {1, 3, 5, 7}
# 对称差(set1 | set2 - set1 & set2)
print(set1 ^ set2)                      # {1, 3, 5, 7, 8, 10}
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}
set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
set1 |= set2  # set1.update(set2)
print(set1)  # {1, 2, 3, 4, 5, 6, 7}
set3 = {3, 6, 9}
set1 &= set3  # set1.intersection_update(set3)
print(set1)  # {3, 6}
set2 -= set1  # set2.difference_update(set1)
print(set2)  # {2, 4}
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}
print(set1 < set2)   # True
print(set1 <= set2)  # True
print(set2 < set3)   # False
print(set2 <= set3)  # True
print(set2 > set1)   # True
print(set2 == set3)  # True
print(set1.issubset(set2))    # True
print(set2.issuperset(set1))  # True, 超集

set1 = {1, 10, 100}
set1.add(1000)
set1.add(10000)
print(set1)  # {1, 100, 1000, 10, 10000}
set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)  # {1, 1000, 10000}
set1.clear()
print(set1)  # set()

set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True

fset = frozenset(range(1,6))  # frozenset({1, 2, 3, 4, 5, 6})