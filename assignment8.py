# 1. 基础类定义
# 定义一个Animal类，包含以下内容：
# - __init__方法：接收age参数，初始化age和name属性（name默认为None）
# - get_age和get_name方法：返回对应属性
# - set_age和set_name方法：设置对应属性（set_name方法应有默认参数）
# - __str__方法：返回"animal:name:age"格式的字符串

class Animal:
    def __init__(self, age, name = None):
        self.age = age
        self.name = name
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, new_age):
        self.age = new_age
        return self.age
    def set_name(self, new_name = None):
        self.name = new_name
        return self.name
    def __str__(self):
        return f'animal:{self.name}:{self.age}'

# 2. 继承练习：猫类
# 定义一个Cat类，继承自Animal类
# - 添加speak方法：打印"meow"
# - 重写__str__方法：返回"cat:name:age"格式
# - 注意：Cat类应继承Animal的所有属性和方法

class Cat(Animal):
    def __init__(self, age, name):
        Animal.__init__(self, age, name)
    def speak(self):
        print('meow')
    def __str__(self):
        return f'cat:{self.name}:{self.age}'

# 3. 继承练习：人类
# 定义一个Person类，继承自Animal类
# - __init__方法：接收name和age参数，调用父类初始化并设置name
# - 添加friends列表属性
# - 添加speak方法：打印"hello"
# - 添加add_friend方法：添加朋友到friends列表
# - 重写__str__方法：返回"person:name:age"格式

class Person(Animal):
    def __init__(self, age, name):
        Animal.__init__(self, age)
        self.name = name
        self.friends = []
    def speak(self):
        print('hello')
    def add_friend(self, new_friend):
        if new_friend in self.friends:
            return 'U had added this friend.'
        else:
            self.friends.append(new_friend)
    def __str__(self):
        return f'person:{self.name}:{self.age}'

# 4. 多重继承：学生类
# 定义一个Student类，继承自Person类
# - __init__方法：接收name, age, major参数，major默认为None
# - 添加change_major方法：修改专业
# - 重写speak方法：随机打印以下四句话之一：
#   "i have homework", "i need sleep", "i should eat", "i am watching tv"
# - 重写__str__方法：返回"student:name:age:major"格式

import random
class Student(Person):
    def __init__(self, name, age, major = None):
        Person.__init__(name, age)
        self.major = major
    def change_major(self, new_major):
        self.major = new_major
    def speak(self):
        print(random.choice(["i have homework", "i need sleep", "i should eat", "i am watching tv"]))
    def __str__(self):
        return f'student:{self.name}:{self.age}+{self.major}'

# 5. 类变量练习：兔子类
# 定义一个Rabbit类，继承自Animal类
# - 添加类变量tag，初始值为1，用于给每个兔子实例分配唯一ID
# - __init__方法：接收age, parent1, parent2参数（parent1和parent2默认为None）
# - 在初始化时，为实例分配rid（使用Rabbit.tag的当前值），然后将Rabbit.tag加1
# - 添加get_rid方法：返回rid（用zfill补零到3位）
# - 添加get_parent1和get_parent2方法
class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2

# 6. 特殊方法重写：兔子相等判断
# 在Rabbit类中添加__eq__方法，判断两只兔子是否相等
# 规则：如果两只兔子的父母相同（parent1和parent2相同，不考虑顺序），则返回True
# 注意：比较父母的rid而不是父母对象本身
# 示例：r1的父母是A和B，r2的父母是B和A，则r1和r2相等

def __eq__(self, other):
    parent_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
    parent_opposite = self.parent1.rid == other.parent2.rid and self.parent2.rid == other.parent1.rid
    return parent_same or parent_opposite

# 7. 特殊方法重写：兔子加法
# 在Rabbit类中添加__add__方法，实现两个兔子实例相加
# 规则：返回一个新的Rabbit实例，age为0，parent1为self，parent2为other

def __add__(self, other):
    return Rabbit(0, self, other)

# 8. 信息隐藏实践
# 修改Animal类，将age属性改名为_years（内部变量）
# 注意：外部不应直接访问_years属性，而是通过getter/setter
class AnimalHidden:
    def __init__(self, age):
        self._years = age

# 9. 类变量与实例变量
# 创建一个Car类，包含以下内容：
# - 类变量wheels，值为4（所有汽车都有4个轮子）
# - __init__方法：接收brand, model参数，初始化实例变量
# - 添加一个类方法get_wheels，返回类变量wheels的值
# - 添加一个实例方法get_info，返回车辆信息

class Car:
    wheels = 4
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    @classmethod
    def get_wheels(self):
        return Car.wheels
    def get_info(self):
        return f'''The car's info:        
Wheels:\t{Car.wheels}
Brand:\t{self.brand}
Model:\t{self.model}'''

# 10. 多层继承体系
# 创建一个Vehicle基类，包含：
# - __init__方法：接收make, year参数
# - get_info方法：返回车辆基本信息
#
# 创建Bicycle类继承Vehicle：
# - 重写__init__方法：添加num_gears参数，调用父类初始化
# - 重写get_info方法：添加档位信息
#
# 创建ElectricBicycle类继承Bicycle：
# - 重写__init__方法：添加battery_capacity参数
# - 重写get_info方法：添加电池信息

class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year
    def get_info(self):
        return f'''The vehicle's info:
Make:\t{self.make}
Year:\t{self.year}'''
class Bicycle(Vehicle):
    def __init__(self, make, year, num_gears):
        Vehicle.__init__(self, make, year)
        self.num_gears = num_gears
    def get_info(self):
        return f'''The bicycle's info:
Make:\t{self.make}
Year:\t{self.year}
Num_gears:\t{self.num_gears}'''
class ElectricBicycle:
    def __init__(self, make, year, num_gears, battery_capacity):
        Bicycle.__init__(self, make, year, num_gears)
        self.battery_capacity = battery_capacity
    def get_info(self):
        return f'''The electricbicycle's info:
Make:\t{self.make}
Year:\t{self.year}
Num_gears:\t{self.num_gears}
Battery_capacity:\t{self.battery_capacity}'''
    
# 11. 多态练习：动物园
# 创建一个函数animal_sounds，接收一个动物列表
# 遍历列表中的每个动物，调用其speak方法（如果没有speak方法则跳过）
# 注意：列表中可以包含Animal、Cat、Person、Student等实例

def animal_sounds(animals):
    for animal in animals:
        if hasattr(animal,"speak"):
            animal.speak()

# 12. 组合与继承
# 创建一个Engine类，包含：
# - __init__方法：接收horse_power参数
# - start方法：打印"Engine started"
# 创建一个CarWithEngine类，继承Car类并包含Engine实例
# - __init__方法：接收brand, model, horse_power参数
#   调用父类初始化，并创建Engine实例作为属性
# - start方法：先调用Engine的start方法，再打印"Car is ready"

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power
    def start(self):
        print('Engine started')
class CarWithEngine(Car):
    def __init__(self, brand, model, horse_power):
        Car.__init__(self, brand, model)
        self.horse_power = Engine(horse_power)
    def start(self):
        self.Engine.start()
        print('Car is ready.')

# 13. 静态方法练习
# 在Rabbit类中添加一个静态方法is_valid_parent
# 该方法接收一个parent参数，返回bool值
# 规则：如果parent是Rabbit实例且年龄大于1岁，返回True，否则返回False

@staticmethod
def is_valid_parent(parent):
    if type(parent) == Rabbit:
        if parent > 1:
            return True
        else:
            return False

# 14. 属性装饰器练习
# 创建一个BankAccount类，使用@property装饰器
# - 将balance设为私有属性
# - 使用@property装饰器创建balance的getter
# - 使用@balance.setter创建setter，确保余额不能设置为负数

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance_setter(self, value):
        if value < 0:
            return 'U cant enter a negative value.'
        else:
            self.balance = value
            return 'U had changed ur balance.'

# 15. 综合练习：学校管理系统
# 创建一个SchoolMember基类，包含：
# - __init__方法：接收name, age参数
# - introduce方法：返回基本信息
# 创建Teacher类继承SchoolMember：
# - 添加subject属性
# - 重写introduce方法：添加所教科目信息
# 创建Class类，包含：
# - __init__方法：初始化班级名称和学生列表
# - add_student方法：添加学生
# - list_students方法：列出所有学生

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f'-Name:\t{self.name}\n Age:\t{self.age}'
class Teacher(SchoolMember):
    def __init__(self, name, age, subject):
        SchoolMember.__init__(self, name, age)
        self.subject = subject
    def introduce(self):
        return f'-Name:\t{self.name}\n Age:\t{self.age}\n Subject:\t{self.subject}'
class Class:
    def __init__(self, class_name, lst_stu = None):
        if lst_stu == None:
            lst_stu = []
        self.class_name = class_name
        self.lst_stu = lst_stu
    def add_student(self, new_member):
        if isinstance(new_member, SchoolMember):
            if new_member not in self.lst_stu:
                self.lst_stu.append(new_member)
    def list_students(self):
        if not self.lst_stu:
            return 'There r no students in this class or u entered a wrong class_name.'
        else:
            result = 'The members in this class r as follows:\n'
            for mem in self.lst_stu[:len(self.lst_stu) - 1]:
                result += f'{mem.introduce()}\n'
            result += f'{self.lst_stu[len(self.lst_stu) - 1].introduce()}'
            return result