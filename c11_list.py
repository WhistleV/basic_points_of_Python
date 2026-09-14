# Simple operation of list:
items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]
print(items1)  # [35, 12, 99, 68, 55, 35, 87]
print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
print(items3)  # [100, 12.3, 'Python', True]
items4 = list(range(1, 10))
items5 = list('hello')
print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(items5)  # ['h', 'e', 'l', 'l', 'o']
items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
items5 += items6
print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']
print(29 in items6)  # True
print(99 in items6)  # False
print('C++' not in items7)     # True
print('Python' not in items7)  # False

# Simple syntax for list:
# Add:
languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')
print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']
languages.insert(1, 'SQL')
print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
addition = ['rust', 'C#']
languages.extend(addition)
languages.append(addition)
print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript', 'rust', 'C#', ['rust', 'C#']]

# Subtract:
languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
languages.pop()
temp = languages.pop(1)
print(temp)       # SQL
languages.append(temp)
print(languages)  # ['Python', C++', 'SQL']
del languages[1]
print(languages)  # ['Python', 'SQL']
languages.clear()
print(languages)  # []
a = [1, 2, 2, 2, 3, 4]
a.remove(2)
print(a)  # [1, 2, 2, 3, 4]

# Others:
items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))     # 0
print(items.index('Python', 1))  # 5
print(items.count('Python'))     # 2
print(items.count('Kotlin'))     # 1
print(items.count('Swfit'))      # 0
print(items.index('Java', 3))    # ValueError: 'Java' is not in list
items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items.sort()
print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
items.reverse()
print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']

# Optimization for 'for-in':
items = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)
items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)