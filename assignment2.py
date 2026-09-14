# 编写程序，要求用户输入姓名、年龄和所在城市
# 然后输出格式化的自我介绍，例如：
# "我叫张三，今年20岁，来自武汉。"
# 要求使用字符串连接或格式化输出

name = input("Enter ur name: ")
age = input("Enter ur age: ")
city = input("Enter ur city: ")
print("我叫" + name + "，今年" + age + "岁，来自" + city + "。")

# 编写程序，让用户输入一个单词和一个数字n
# 程序输出该单词重复n次的结果
# 例如：输入"hello"和3，输出"hellohellohello"

word = input("Enter a word in random: ")
num = int(input("Enter a number in random: "))
print(word * num)

# 编写程序，输入一个0-100的分数
# 根据分数输出等级：
# 90-100: 优秀
# 80-89: 良好  
# 70-79: 中等
# 60-69: 及格
# 60以下: 不及格
# 要求使用if-elif-else结构

score = int(input("Enter a number between 0 and 100: "))
if score >=90:
    print("优秀")
elif score >=80:
    print("良好")
elif score >=70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 编写简单的登录验证程序
# 预设用户名"admin"，密码"123456"
# 要求用户输入用户名和密码
# 如果都正确，输出"登录成功"
# 如果用户名错误，输出"用户名不存在"
# 如果密码错误，输出"密码错误"

correct_username = "admin"
correct_password = "123456"
username = input("Enter ur username: ")
password = input("Enter ur password: ")
if username == correct_username and password == correct_password:
    print("登录成功")
elif username != correct_username:
    print("用户名不存在")
else:
    print("密码错误")

# 改进课件中的猜年份游戏
# 设置一个1-100的随机数字作为答案
# 让用户反复猜测，并给出"太大"或"太小"的提示
# 直到猜对为止，统计猜测次数并输出

import random
answer = random.randint(1,100)
attempts = 1
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < answer:
        print("Too small!")
        attempts += 1
    elif guess > answer:
        print("Too big!")
        attempts += 1
    else:
        print("U r right! And ur number of seeking attempts is",attempts)
        break

# 使用while循环实现：
# 让用户反复输入数字，输入0时停止
# 计算所有输入数字的总和并输出
# 同时统计输入了多少个数字（不包括0）

quantity = 0
sum = 0
while True:
    try:
        i = int(input("Enter a number: "))
        if i == 0:
            break
        else:
            quantity += 1
            sum += i
    except ValueError:
        print("Please enter a valid integer.")
print("The sum of numbers u entered is: ",sum," and the quantity is: ",quantity)

# 使用for循环和range函数
# 输出5的乘法表：5×1=5, 5×2=10, ..., 5×9=45

n = 5
for i in range(1,10):
    result = n * i
    print(n,"*",i,"=",result)

# 进阶：让用户输入数字n，输出n的乘法表

try:
    n = int(input("Enter a number: "))
    for i in range(1,10):
            result = n * i
            print(n,"*",i,"=",result)
except ValueError:
        print("Please enter a valid integer.")

# 使用for循环计算：
# 1. 1-100所有整数的和
# 2. 1-100所有奇数的和  
# 3. 1-100所有3的倍数的和
# 分别输出三个结果

Result1 = 0
Result2 = 0
Result3 = 0
for i in range(1,101):
    Result1 += i
print("Result1 =",Result1)
for j in range(1,101,2):
    Result2 += j
print("Result2 =",Result2)
for k in range(0,101,3):
    Result3 += k
print("Result3 =",Result3)

# 编写程序判断输入的数字是否为质数
# 使用for循环遍历2到n-1的所有数字
# 如果发现能整除的数，立即break并输出"不是质数"
# 如果循环完成都没有break，输出"是质数"

try:
    n = int(input("Enter a number: "))
    for i in range(2,n):
        if n % i == 0:
            print("不是质数")
            break
    else:
        print("是质数")
except ValueError:
    print("Please enter a valid integer.")

# 生成一个1-50的随机数列表
# 让用户输入要查找的数字
# 使用for循环遍历列表，找到目标数字时立即break
# 输出是否找到以及查找的步数

import random
list1 = list(range(1,51))
random.shuffle(list1)
try:
    target = int(input("Enter a number: "))
    steps = 0
    indicator = False
    for i in list1:
        steps += 1
        if i == target:
            indicator = True
            break
    if indicator:
        print("Found the number in",steps,"steps.")
    else:
        print("Number is not founded.")
except ValueError:
    print("please enter a valid integer.")

# 编写一个持续运行的计算器程序
# 每次循环让用户选择操作（+,-,*,/）或输入'q'退出
# 根据选择进行相应的数学运算
# 使用while True循环和break语句控制退出

try:    
    num1 = float(input("Enter the original number: "))
    while True:
        operation = input("Choose an operation (+, -, *, /) or 'q' to quit: ")
        if operation == 'q':
            print("Exiting the calculator. Goodbye!")
            break
        try:
            num2 = float(input("Enter the next number: "))
            if operation == '+':
                print("Result:", num1 + num2)
                num1 = num1 + num2
            elif operation == '-':
                print("Result:", num1 - num2)
                num1 = num1 - num2
            elif operation == '*':
                print("Result:", num1 * num2)
                num1 = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    print("Result:", num1 / num2)
                    num1 = num1 / num2
                else:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid operation. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
except ValueError:
    print("please enter a valid number.")

# 使用嵌套循环打印以下图案：
# *
# **
# ***
# ****
# *****
# 让用户输入行数n，打印n行的三角形

while True:
    try:
        n = int(input("Enter the number of rows: "))
        if n <= 0:
            print("Please enter a positive integer.")
            continue
        for i in range(1,n+1):
            print("*"*i)
        break
    except ValueError:
        print("Please enter a valid integer.")