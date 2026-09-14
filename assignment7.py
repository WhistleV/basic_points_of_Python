# 1. 基本类定义
# 定义一个名为Person的类，包含以下内容：
# - __init__方法：接收name和age参数，并保存为实例属性
# - introduce方法：返回字符串"我叫{name}，今年{age}岁"
# - __str__方法：返回与introduce方法相同的字符串

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"My name is {self.name} and im {self.age} this year."
    def __str__(self):
        return f"My name is {self.name} and im {self.age} this year."

# 2. 二维向量类
# 定义一个Vector2D类，表示二维向量(x, y)
# - __init__方法：初始化x和y属性
# - __add__方法：实现向量加法，返回新向量
# - __sub__方法：实现向量减法，返回新向量
# - magnitude方法：计算向量的模（长度），公式：sqrt(x^2 + y^2)
# - __str__方法：返回格式"Vector2D(x, y)"

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x1 = self.x + other.x
        y1 = self.y + other.y
        return Vector2D(x1, y1)
    def __sub__(self, other):
        x2 = self.x - other.x
        y2 = self.y - other.y
        return Vector2D(x2, y2)
    def magnitude(self):
        from math import sqrt
        return sqrt(self.x ** 2 + self.y **2)
    def __str__(self):
        return f'Vector2D({self.x}, {self.y})'

# 3. 矩形类
# 定义一个Rectangle类，表示矩形
# - __init__方法：接收width和height参数，保存为实例属性
# - area方法：计算面积
# - perimeter方法：计算周长
# - __str__方法：返回格式"Rectangle(width, height)"
# - __eq__方法：比较两个矩形面积是否相等

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def __str__(self):
        return f'Rectangle({self.width}, {self.height})'
    def __eq__(self, other):
        if self.width * self.height == other.width * other.height:
            return True
        else:
            return False

# 4. 银行账户类
# 定义一个BankAccount类，模拟银行账户
# - __init__方法：接收account_holder和balance参数，balance默认为0
# - deposit方法：存款，增加余额
# - withdraw方法：取款，减少余额（余额不足时打印提示）
# - __str__方法：返回账户信息
# - 添加一个类属性interest_rate（利率），值为0.02

class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance
    interest_rate = 0.02
    def deposit(self, amount):
        if amount < 0:
            return 'Invalid operation.'
        else:
            self.balance += amount
            return self.balance
    def withdraw(self, amount):
        if amount < 0:
            return 'Invalid operation.'
        if self.balance < amount:
            return 'Insufficient balance.'
        else:
            self.balance -= amount
            return self.balance
    def __str__(self):
        return f'''
Account_holder:\t{self.account_holder}
balance:\t{self.balance}
interest_rate:\t{self.interest_rate}'''
    
# 5. 学生类（包含类属性）
# 定义一个Student类，包含以下内容：
# - 类属性school_name，值为"中国地质大学"
# - __init__方法：接收name, student_id, major参数
# - get_info方法：返回学生完整信息（包括学校、姓名、学号、专业）
# - 类方法change_school：可以修改所有学生的学校名称

class Student:
    school_name = 'China University of Geoscience'
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
    def get_info(self):
        return f'''School:\t{self.school_name}
Name:\t{self.name}
Student_id:\t{self.student_id}
Major:\t{self.major}'''
    def change_school(self):
        self.school_name = input('Enter a new school_name: ')
        return 'Operation complete.'

# 6. 分数类（特殊方法）
# 定义一个Fraction类，表示分数
# - __init__方法：接收num和denom参数（分子和分母）
# - __add__方法：实现分数加法，返回新分数（需约分）
# - __sub__方法：实现分数减法，返回新分数（需约分）
# - __mul__方法：实现分数乘法，返回新分数（需约分）
# - __str__方法：返回"分子/分母"形式
# - to_float方法：返回小数形式
# 提示：约分可以使用math.gcd函数

import math
class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom    
    def __add__(self, other):
        new_num_temp = self.num + other.num
        new_denom_temp = self.denom + other.denom
        if new_denom_temp == 0:
            return 'Zero cant be denom.'
        new_num, new_denom =new_num_temp // math.gcd(new_num_temp, new_denom_temp), new_denom_temp // math.gcd(new_num_temp, new_denom_temp)
        return Fraction(new_num, new_denom)
    def __sub__(self, other):
        new_num_temp = self.num - other.num
        new_denom_temp = self.denom - other.denom
        if new_denom_temp == 0:
            return 'Zero cant be denom.'
        new_num, new_denom =new_num_temp // math.gcd(new_num_temp, new_denom_temp), new_denom_temp // math.gcd(new_num_temp, new_denom_temp)
        return Fraction(new_num, new_denom)
    def __mul__(self, other):
        new_num_temp = self.num * other.num
        new_denom_temp = self.denom * other.denom
        if new_denom_temp == 0:
            return 'Zero cant be denom.'
        new_num, new_denom =new_num_temp // math.gcd(new_num_temp, new_denom_temp), new_denom_temp // math.gcd(new_num_temp, new_denom_temp)
        return Fraction(new_num, new_denom)
    def __str__(self):
        if self.denom == 0:
            return'Zero cant be denom.'
        elif self.denom == 1:
            return f'{self.num}'
        elif self.denom == -1:
            return f'{-self.num}'
        else:    
            return f'{self.num}/{self.denom}'
    def to_float(self):
        return f'{self.num / self.denom:.2f}'

# 7. 购物车类
# 定义一个ShoppingCart类，模拟购物车功能
# - __init__方法：初始化一个空字典用于存储商品（商品名:数量）
# - add_item方法：添加商品，接收商品名和数量
# - remove_item方法：移除商品，接收商品名和数量（数量不足时完全移除）
# - get_total_items方法：返回购物车中商品总数
# - __str__方法：返回购物车内容

class ShoppingCart:
    def __init__(self):
        self.cart = {}
    def add_item(self, goods_name, quantity = 1):
        if quantity < 1:
            return 'Please enter a valid quantity.'
        elif goods_name in self.cart:
            self.cart[goods_name] += quantity
            return f'It had been added {quantity} {goods_name}(s), now the quantity of {goods_name} is {self.cart[goods_name]}.'
        else:
            self.cart[goods_name] = quantity
            return f'It had been added {quantity} {goods_name}(s), now the quantity of {goods_name} is {quantity}.'
    def remove_item(self, goods_name, quantity = 1):
        if quantity < 1:
            return 'Please enter a valid quantity.'
        elif goods_name in self.cart:
            if quantity <= self.cart[goods_name]:
                self.cart[goods_name] -= quantity
                return f'It had been removed {quantity} {goods_name}(s), now the quantity of {goods_name} is {self.cart[goods_name]}.'
            else:
                del self.cart[goods_name]
                return 'The remaining quantity is insufficient, so the operation deleted the entire commodity.'
        else:
            return 'The shoppingcart doesnt have the commodity, please check ur operation.'
    def get_total_items(self):
        sUm = sum(self.cart.values())
        return f'The total quantity of the shoppingcart is {sUm}.'
    def __str__(self):
        if self.cart == {}:
            return 'The shoppingcart is empty.'
        else:
            result = 'THE SHOPPINGCART CONTENT:\n'
            for i, j in zip(self.cart, range(1, len(self.cart) + 1)):  # for index, (item_name, quantity) in enumerate(self.cart.items(), 1):
                result += f'{j}. {i}: {self.cart[i]}\n'  # result += f'{index}. {item_name}: {quantity}\n'
            result += f'It totally has {len(self.cart)} kind(s) of goods. {self.get_total_items()}'
            return result

# 8. 时间类
# 定义一个Time类，表示时间（时、分、秒）
# - __init__方法：接收hour, minute, second参数，确保时间合法
# - __add__方法：实现时间相加，考虑进位（60秒进1分，60分进1小时，24小时归零）
# - __str__方法：返回"HH:MM:SS"格式（两位数显示）
# - to_seconds方法：将时间转换为总秒数

class Time:
    def __init__(self, hour, min, sec):
        hour = int(hour)
        min = int(min)
        sec = int(sec)
        min += sec // 60
        sec -= sec // 60 * 60
        hour += min // 60
        min -= min // 60 * 60
        hour -= hour // 24 * 24
        self.hour = hour
        self.min = min
        self.sec = sec
    def __add__(self, other):
        new_sec = self.sec + other.sec
        new_min = self.min + other.min + new_sec // 60
        new_sec -= new_sec // 60 * 60
        new_hour = self.hour + other.hour + new_min // 60
        new_min -= new_min // 60 * 60
        new_hour -= new_hour // 24 * 24
        return Time(new_hour, new_min, new_sec)
    def __str__(self):
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}' 
    def to_second(self):
        result = self.hour * 60 * 60 + self.min * 60 + self.sec
        return f'The total seconds: {result}s.'
    
# 9. 图书类与图书馆类（两个类交互）
# 先定义一个Book类：
# - __init__方法：接收title, author, isbn参数
# - __str__方法：返回图书信息
# 
# 再定义一个Library类：
# - __init__方法：初始化一个空列表存储图书
# - add_book方法：添加图书
# - remove_book方法：根据ISBN移除图书
# - find_books_by_author方法：根据作者查找图书
# - __str__方法：返回图书馆所有图书信息

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def __str__(self):
        return f"The book's info:\nTitle:\t{self.title}\nAuthor:\t{self.author}\nISBN:\t{self.isbn}"
    def __repr__(self):
        return f'<<{self.title}>>-{self.author}-{self.isbn}'
class Library:
    def __init__(self):
        self.lst = []
    def add_book(self, new_book):
        if not isinstance(new_book, Book):
            return f'The type of {new_book} must be Book.'
        else:
            for i in self.lst:
                if i.isbn == new_book.isbn:
                    return 'The library has had the book already.'
            else:
                self.lst.append(new_book)
                return f'Had added: {new_book.title}'
    def remove_book(self, search_isbn):
        for j,i in enumerate(self.lst):
            if i.isbn == search_isbn:
                del self.lst[j]
                return f'Had removed {i.title}'
        else:
            return 'The book u wanna removed isnt in the library.'
    def find_books_by_author(self, search_author):
        found_book = [i for i in self.lst if i.author == search_author]
        if not found_book:
            return 'Sorry, the library doesnt have this book.'
        else:
            return f'Had found: {found_book}'
    def __str__(self):
        if not self.lst:
            return 'The library is empty.'
        else:
            result = 'All the books in the library are as follows:\n'
            for i in self.lst[:len(self.lst) - 1]:
                result += f'<<{i.title}>>-{i.author}-{i.isbn}\n'
            result += f'<<{self.lst[-1].title}>>-{self.lst[-1].author}-{self.lst[-1].isbn}'
            return result