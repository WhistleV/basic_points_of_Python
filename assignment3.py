# 编写程序，输入一个字符串，输出以下信息：
# 1. 字符串长度
# 2. 第一个字符和最后一个字符
# 3. 字符串反转
# 4. 字符串中字母'a'出现的次数

str1ng = input("Enter a string: ")
times = 0
print(len(str1ng))
print(str1ng[0],str1ng[-1])
print(str1ng[::-1])
for i in str1ng:
    if i == 'a':
        times += 1
print("这串字符串中'a'出现了",times,"次。")

# 编写程序，输入一个字符串和两个整数n、m
# 输出该字符串的以下切片：
# 1. 前n个字符
# 2. 后m个字符  
# 3. 从第n个到第m个字符
# 4. 每隔一个字符取一个
# 5. 字符串反转

try:
    str1ng = input("Enter a string: ")
    m = int(input("Enter an integer: "))
    n = int(input("Enter a less integer: "))
    if n < m and m > 0 and n > 0:
        print(str1ng[:n])
        print(str1ng[-m:])
        print(str1ng[n - 1:m])
        print(str1ng[::2])
        print(str1ng[::-1])
    else:
        print("Check whether the second number is less than the first number or the two numbers are both bigger than 0")
except ValueError:
    print("Please enter a valid integer.")

# 编写程序，检查输入的字符串是否满足：
# 1. 至少包含一个大写字母
# 2. 至少包含一个小写字母  
# 3. 至少包含一个数字
# 4. 长度至少为8个字符
# 输出检查结果（哪些条件满足，哪些不满足）

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"

str1ng = input("Enter a string: ")
con1 = "没有满足'至少包含一个大写字母'"
con2 = "没有满足'至少包含一个小写字母'"
con3 = "没有满足'至少包含一个数字'"
con4 = "没有满足'长度至少为8个字符'"
for i in str1ng:
    if i in LETTERS:
        con1 = "满足'至少包含一个大写字母'"
        break
for j in str1ng:
    if j in letters:
        con2 = "满足'至少包含一个小写字母'"
        break
for k in str1ng:
    if k in num:
        con3 = "满足'至少包含一个数字'"
        break
if len(str1ng) >= 8:
    con4 = "满足'长度至少为8个字符'"
print(f"该字符串{con1}、{con2}、{con3}、{con4}。")

# 使用穷举法找出1-1000之间的所有完全平方数
# 完全平方数：能够表示成某个整数的平方的数
# 输出所有找到的完全平方数

i = 1
num_square = ""
while i ** 2 <= 1000:
    if num_square:
        num_square += " "
    num_square += str(i ** 2)
    i += 1
print(f"the squares between 1 and 1000 are {num_square}")

# 使用穷举法找出所有的3位水仙花数
# 水仙花数：一个3位数，其各位数字立方和等于该数本身
# 例如：153 = 1^3 + 5^3 + 3^3

result = []
for i in range(100,1000):
    i_str = str(i)
    if i == int(i_str[0]) ** 3 + int(i_str[1]) ** 3 + int(i_str[2]) ** 3:
        result.append(i)
print(result)

# 输入一个正整数，使用穷举法找出它的所有因子
# 例如：输入12，输出1, 2, 3, 4, 6, 12

Factor = []
i = 1
try:
    num = int(input("Enter a positive integer: "))
    while i <= num ** 0.5:
        if num % i == 0:
            n = num / i
            n = int(n)
            Factor.append(i)
            if i != num // i:
                Factor.append(n)
        i += 1
    Factor.sort()
    print(Factor)
except ValueError:
    print("Please enter a valid number.")

# 使用近似法计算一个正数的平方根
# 设置epsilon = 0.01，increment = 0.0001
# 输出近似结果和猜测次数
# 与math.sqrt()的结果比较

pnum = float(input("Enter a positive number greater than or equal to 1: "))
if pnum < 1:
    print("Please enter a valid number.")
epsilon = 10 ** -2
increment = 10 ** -4
attempts = 0
gnum = 0
while abs(pnum - gnum ** 2) >= epsilon and gnum  < pnum:
    gnum += increment
    attempts += 1
print(f"It tried {attempts} times.")
if abs(pnum - gnum ** 2) >= epsilon:
    print("We didnt find the correct answer.")
else:
    print(f"The approximation is {gnum:.4f}")
import math
print(f"The math.sqrt() result is {math.sqrt(pnum):.4f}")

# 使用近似法求方程 x^2 + x - 1 = 0 在[0,1]区间的近似解
# 设置epsilon = 0.001
# 输出近似解和猜测次数

x = 0
attempts = 0
epsilon = 10 ** -4
increment = 10 ** -4
while abs(x ** 2 + x - 1) >= 0.0001 and x <= 1:
    attempts += 1
    x += increment
print(f"It tried {attempts} times.")
if abs(x * 2 + x - 1) >= 0.001:
    print("We didnt find the correct answer.")
else:
    print(f"The approximation is {x:.4f}")

# 使用二分法求方程 x^3 - x - 1 = 0 在[1,2]区间的根
# 设置epsilon = 0.0001
# 输出近似解和迭代次数

attempts = 0
epsilon = 10 ** -4
x_low = 1
x_high  = 2
x = (x_low + x_high)/2
while abs(x ** 3 - x - 1) >= 10 ** -4:
    if (x ** 3 - x - 1) < 0:
        x_low = x
    else:
        x_high = x
    attempts += 1
    x = (x_low + x_high)/2
print(f"It tried {attempts} times. And the approximatation of x is {x:.4f}")

# 结合字符串操作和穷举思想
# 检查密码强度，根据以下规则评分：
# - 长度>=8: +1分
# - 包含大写字母: +1分  
# - 包含小写字母: +1分
# - 包含数字: +1分
# - 包含特殊字符: +1分
# 输出密码强度等级（弱：0-2分，中：3分，强：4-5分）

point = 0
password = input("Enter ur password: ")
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
for i in password:
    if i in LETTERS:
        point += 1
for j in password:
    if j in letters:
        point += 1
for k in password:
    if k in num:
        point += 1
for l in password:
    if l not in LETTERS and l not in letters and l not in num:
        point += 1
if len(password) >= 8:
    point += 1
if point == 0 or point == 1 or point == 2:
    print("The  level of password strength is low.")
elif point == 3:
    print("The level of password strength is intermediate.")
else:
    print("The level of password strength is high.")