class Student:
    __slots__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age
stu = Student('王大锤', 20)
# AttributeError: 'Student' object has no attribute 'sex'
stu.sex = '男'

class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    @staticmethod
    def is_valid1(a, b, c):
        return a + b > c and b + c > a and a + c > b
    @classmethod
    def is_valid2(cls, a, b, c):
        return a + b > c and b + c > a and a + c > b 
    @property
    def perimeter(self):
        return self.a + self.b + self.c
    @property
    def area(self):
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
t = Triangle(3, 4, 5)
print(f'C: {t.perimeter}')
print(f'S: {t.area}')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f'{self.name} is having meals.')
    def sleep(self):
        print(f'{self.name} is sleeping.')
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)  # Person.__init__(name, age)
    def study(self, course_name):
        print(f'{self.name} is learning {course_name}.')
class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title
    def teach(self, course_name):
        print(f'{self.name}{self.title} is teaching {course_name}.')