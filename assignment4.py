# 1.1 编写一个函数 is_positive()，接收一个整数参数，如果参数为正数返回True，否则返回False
#     要求：添加适当的文档字符串说明函数功能

def is_positive(x):
    """
    Input: x, an integer.
    Return True if x is positive, otherwise False.
    """
    return x > 0
try:
    while True:
        x = int(input("Enter an integer as x: "))
        if x == 0:
            print("'x == 0' is invalid. Please reassign x.")
            continue
        print(f"'x is positive': {is_positive(x)}.")
        break
except ValueError:
    print("Please enter a valid integer.")

# 1.2 编写一个函数 calculate_circle(radius)，接收半径参数，返回圆的周长和面积（π取3.14159）
#     要求：使用单个return语句返回两个值

pi = 3.14159
def calculate_circle(radius):
    """
    Input: radius, a positive number.
    Return 2 * pi * radius, pi * radius ** 2
    """
    return 2 * pi * radius, pi * radius ** 2
while True:
    radius = float(input("Please enter a number as radius of a circle: "))
    if radius <= 0:
        print("Please enter a valid positive number.")
        continue
    else:
        x, y = calculate_circle(radius)
        break
print(f"C = {x}")
print(f"S = {y}")

# 2.1 将课件中的立方根计算代码重构为函数 cube_root(number, epsilon)
#     函数接收两个参数：要计算立方根的数字和精度epsilon，返回计算结果和迭代次数

def cube_root(number, epsilon):
    attempts = 0
    high = abs(number) + 1
    low = - abs(number) - 1
    guess = (high + low) / 2
    while abs(guess ** 3 - number) >= epsilon:
        if guess ** 3 - number > 0:
            high = guess
        else:
            low = guess
        guess = (high + low) / 2
        attempts += 1
    if abs(guess ** 3 -number) >= epsilon:
        return("We didnt find the correct answer.")
    else:
        return(f"We found the correct answer is {guess} via the try of {attempts} time(s).")
try:
    number = float(input("Please enter a number: "))
    epsilon = float(input("Please enter the epsilon: "))
except ValueError:
    print("Please enter valid numbers.")    
print(cube_root(number, epsilon))

# 2.2 编写一个主程序，让用户输入多个数字，分别计算它们的立方根并输出
#     体会分解带来的好处：主程序逻辑更清晰，计算部分可复用

def cube_root(number):
    epsilon = 0.0001
    high = abs(number) + 1
    low = - abs(number) - 1
    guess = (high + low) / 2
    while abs(guess ** 3 - number) >= epsilon:
        if guess ** 3 - number > 0:
            high = guess
        else:
            low = guess
        guess = (high + low) / 2
    if abs(guess ** 3 -number) >= epsilon:
        return("We didnt find the correct answer.")
    else:
        return(guess)
results = []
l_number = []
while True:
    try:
        willingness = input("Enter 'q' to quit. Enter others means the input will continue: ")
        if willingness == 'q':
            break
        number = float(input("Please enter a number: "))
    except ValueError:
        print("Please enter valid a number.")
    results.append(cube_root(number))
    l_number.append(number)
print(f"The cube roots of {l_number} r {results}")

# 3 分析以下代码，预测输出结果，然后运行验证
#   answer prediction: x = 5; z = 9
#   Verification: correct

def outer_func(x):
    def inner_func():
        y = x * 2
        return y
    result = inner_func()
    return result + x
x = 5
z = outer_func(3)
print(f"全局变量 x = {x}")
print(f"函数返回值 z = {z}")

# 4 编写一个函数 process_data(data, multiplier=1)，演示默认参数的使用
#   函数功能：如果data是数字，乘以multiplier；如果是字符串，重复multiplier次

def process_data(data, multiplier = 1):
    if type(data) == int or type(data) == float or type(data) == str:
        data *= multiplier
        return data
    else:
        return("An error occurred in the program.")
    
# 5 温度转换系统
#   目标：设计一个温度转换程序，支持摄氏度(C)、华氏度(F)、开尔文(K)之间的相互转换
#   要求：
#   1. 将不同转换功能分解为独立函数：
#      - celsius_to_fahrenheit(c)
#      - fahrenheit_to_celsius(f)
#      - celsius_to_kelvin(c)
#      - kelvin_to_celsius(k)
#      - 其他转换函数（按需添加）
#   2. 设计一个主函数作为程序入口，提供用户交互界面：
#      ========== 温度转换系统 ==========
#      1. 摄氏度 → 华氏度
#      2. 华氏度 → 摄氏度
#      3. 摄氏度 → 开尔文
#      4. 开尔文 → 摄氏度
#      5. 退出系统
#      =================================
#   3. 使用抽象思想：主程序只需要知道如何调用转换函数，不需要知道具体转换公式
#      提示：先设计函数接口，再实现具体功能

def celsius_to_fahrenheit(c):
    f = 1.8 * c + 32
    return f
def fahrenheit_to_celsius(f):
    c = (f - 32) / 1.8
    return c
def celsius_to_kelvin(c):
    k = c + 273.15
    return k
def kelvin_to_celsius(k):
    c = k - 273.15
    return c
def fahrenheit_to_kelvin(f):
    k = (f + 459.67) / 1.8
    return k
def kelvin_to_fahrenheit(k):
    f = 1.8 * k - 459.67
    return f
print("======== 温度转换系统 ========\n1.摄氏度》华氏度\n2.华氏度》摄氏度\n3.摄氏度》开尔文\n4.开尔文》摄氏度\n5.华氏度》开尔文\n6.开尔文》华氏度\n7.退出系统\n=========================")
try: 
    while True:
        option = int(input("Enter ur option: "))
        if option == 1:
            c = float(input("Enter the celsius(°C): "))
            print(f"The corresponding fahrenheit is {celsius_to_fahrenheit(c)}°F.")
        elif option == 2:
            f = float(input("Enter the fahrenheit(°F): "))
            print(f"The corresponding celsius is {fahrenheit_to_celsius(f)}°C.")
        elif option == 3:
            c = float(input("Enter the celsius(°C): "))
            print(f"The corresponding kelvin is {celsius_to_kelvin(c)}K.")
        elif option == 4:
            k = float(input("Enter the kelvin(K): "))
            print(f"The corresponding celsius is {kelvin_to_celsius(k)}°C.")
        elif option == 5:
            f = float(input("Enter the fahrenheit(°F): "))
            print(f"The corresponding kelvin is {fahrenheit_to_kelvin(f)}K.")
        elif option == 6:
            k = float(input("Enter the kelvin(K): "))
            print(f"The corresponding fahrenheit is {kelvin_to_fahrenheit(k)}°F.")
        elif option == 7:
            print("Quit already.")
            break
        else:
            print("Enter a valid option.")
except ValueError:
    print("An error occurred in the program.")
    
# 6 创建一个高阶函数 apply_operation(x, y, operation)
#   该函数接收两个数字和一个函数参数operation，返回operation(x, y)的结果

def apply_operation(x, y, ope):
    if ope == '+':
        result = x + y
    elif ope == '-':
        result = x - y
    elif ope == '*':
        result = x * y
    elif result == '/':
        result = x / y
    return result
x = float(input("Enter a number: "))
while True:
    ope = input("Enter the operation notation: ")
    if ope != '+' and ope != '-' and ope != '*' and ope != '/':
        print("Please enter a valid operation notation.")
        continue
    break    
while True:  
    y = float(input("Enter the next number: "))        
    if y == 0:
        print("Division by zero is illegal. Please enter a number except zero.")
        continue
    break 
print(f"{x} {ope} {y} = {apply_operation(x, y, ope)}")

# 7 目标：运用分解和抽象思想，设计一个学生成绩分析系统
#   要求：
#   1. 分解为以下模块（函数）：
#    - input_grades(): 输入学生成绩（返回列表）
#    - calculate_average(grades): 计算平均分
#    - find_max_min(grades): 查找最高分和最低分
#    - count_grade_levels(grades): 统计各等级人数（A:90+, B:80-89, C:70-79, D:60-69, F:<60）
#   2. 设计主程序流程：
#      a. 输入学生成绩
#      b. 计算各项统计指标
#      c. 显示分析结果
#   示例输出：
#   ========== 成绩分析系统 ==========
#   学生成绩：[85, 92, 78, 90, 88]
#   分析结果：
#   - 平均分：86.6
#   - 最高分：92，最低分：78
#   - 等级分布：A(2人) B(2人) C(1人) D(0人) F(0人)
#   ================================

def input_grades():
    lst_str = input("Enter students_grades, separate with spaces: ")
    lst = [int(x) for x in lst_str.split(' ')]
    return lst
def calculate_average(lst):
    sum_grades = sum(lst)
    num_students = len(lst)
    avg = sum_grades / num_students
    return avg
def find_max_min(lst):
    max_temp = max(lst)
    min_temp = min(lst)
    return max_temp, min_temp
def count_grade_levels(lst):
    A_count = B_count = C_count = D_count = E_count = 0
    for _ in lst:
        if _ >= 90:
            A_count +=1
        elif _ >= 80 and _ < 90:
            B_count += 1
        elif _ >= 70 and _ <80:
            C_count += 1
        elif _ >= 60 and _ < 70:
            D_count += 1
        else:
            E_count += 1
    return A_count, B_count, C_count, D_count, E_count
lst = input_grades()
avg = calculate_average(lst)
max, min = find_max_min(lst)
A, B , C, D, E = count_grade_levels(lst)
print(f"========== 成绩分析系统 ==========\n学生成绩: {lst}\n分析结果:\n- 平均分: {avg:.1f}\n- 最高分: {max}, 最低分: {min}\n- 等级分布: A({A}人) B({B}人) C({C}人) D({D}人) E({E}人)\n================================")