person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101'
}
person = dict(name='王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋101')
items1 = dict(zip('ABCDE', '12345'))
print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.get('name'))       # 王大锤
print(person.get('sex'))        # None
person = {'name': '王大锤', 'age': 25, 'height': 178}
print(person.keys())    # dict_keys(['name', 'age', 'height'])
print(person.values())  # dict_values(['王大锤', 25, 178])
print(person.items())   # dict_items([('name', '王大锤'), ('age', 25), ('height', 178)])
for key, value in person.items():
    print(f'{key}:\t{value}')

person1 = {'name': '王大锤', 'age': 55, 'height': 178}
person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
person1 |= person2  # person1.update(person2)
print(person1)  # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}

person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.pop('age'))  # 25
print(person)             # {'name': '王大锤', 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.popitem())   # ('addr', '成都市武侯区科华北路62号1栋101')
print(person)             # {'name': '王大锤', 'height': 178}
person.clear()
print(person)             # {}
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
del person['age']
del person['addr']
print(person)  # {'name': '王大锤', 'height': 178}