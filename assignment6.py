# 1. 递归乘法函数
# 编写一个递归函数multiply(a, b)，不使用乘法运算符(*)，
# 通过递归计算两个正整数a和b的乘积。
# 基本情形：当b == 1时，返回a
# 递归情形：返回a + multiply(a, b-1)

def multiply(a, b):
    if b == 1:
        return a
    else:
        return a + multiply(a, b - 1)

# 2. 递归阶乘函数
# 编写一个递归函数factorial(n)，计算n的阶乘。
# 基本情形：n == 0或n == 1时，返回1
# 递归情形：返回n * factorial(n-1)
# 要求：当n为负数时返回None

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return None
    else:
        return n * factorial(n - 1)
    

# 3. 斐波那契数列（基础版与优化版）
# 3.1 编写朴素递归函数fib(n)，计算斐波那契数列第n项（定义：fib(1)=1, fib(2)=1, fib(n)=fib(n-1)+fib(n-2)）
# 3.2 使用字典优化，编写函数fib_memo(n, memo={})，通过字典存储已计算的结果避免重复计算

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n -2)

def fib_memo(n, memo=None):
    if memo == None:
        memo == {}
    elif n == 1 or n == 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        return memo[n]

# 4. 递归回文判断
# 编写递归函数is_palindrome(s)，判断字符串s是否为回文（忽略大小写和非字母字符）。
# 要求：先编写辅助函数clean_string(s)清理字符串（转小写、去除非字母字符），
# 然后编写递归函数check_palindrome(s)判断是否为回文。

def clean_string(s_original):
    s = ""
    for i in s_original:
        i = i.lower()
        if i in "abcdefghijklmnopqrstuvwxyz":
            s += i
        return s
def check_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        return s[0] == s[-1] and check_palindrome(s[1:-1])            
def is_palindrome():
    s = clean_string(s_original)
    return check_palindrome(s) 
s_original = "Able was I, ere I saw Elba."
print(is_palindrome())

# 5. 递归列表操作
# 5.1 编写递归函数recursive_sum(lst)，计算列表中所有数字的和。
# 5.2 编写递归函数find_max(lst)，找出列表中的最大值。

def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + lst[1:]
def find_max(lst):
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        return lst[0] if lst[0] > find_max[1:] else find_max[1:]

# 6. 字典基本操作
# 创建一个学生成绩字典，完成以下操作：
# 1) 创建字典grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
# 2) 添加学生'Sylvan'，成绩为'A'
# 3) 修改'John'的成绩为'A'
# 4) 删除'Ana'的记录
# 5) 检查'Daniel'是否在字典中
# 6) 获取所有学生姓名列表
# 7) 获取所有成绩列表
# 8) 获取(姓名, 成绩)对的列表

def dict_operations():
    grades = {'Ana': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A'}
    grades['Sylvan'] = 'A'
    grades['John'] = 'A'
    del grades['Ana']
    isin_dict = 'Daniel' in grades
    print(f'Daniel is in dict: {isin_dict}')
    print(grades.keys())
    print(grades.values())
    print(grades.items())

# 7. 单词频率统计
# 编写函数word_frequency(text)，统计一段文本中每个单词的出现频率。
# 要求：不区分大小写（所有单词转小写），去除标点符号（只保留字母和空格）
# 返回字典：键为单词，值为出现次数

def word_frequency(text):
    text = text.lower()
    text1 = ''
    for i in text:
        if i in 'abcdefghijklmnopqrstuvwxyz ':
            text1 += i
    text_list = text1.split(' ')
    words = {}
    for i in text_list:
        if i not in words:
            words[i] = 1
        elif i in words:
            words[i] += 1
    return words
text = "Life is a journey, and the journey continues."
print(word_frequency(text))
    
# 8. 字典合并与反转
# 8.1 编写函数merge_dicts(dict1, dict2)，合并两个字典，相同键的值相加
# 8.2 编写函数reverse_dict(d)，将字典的键和值互换（注意处理值重复的情况）

def merge_dicts(dict1, dict2):
    for i in dict2:
        if i in dict1:
            dict1[i] += dict2[i]
        else:
            dict1[i] = dict2[i]
    return dict1
def reverse_dict(d):
    d1 = {}
    for i in d:
        if d[i] not in d1:
            d1[d[i]] = i

# 9. 递归列表扁平化
# 编写递归函数flatten_list(lst)，将任意嵌套列表扁平化为单层列表。
# 例如：输入[1, [2, [3, 4], 5], 6] 返回[1, 2, 3, 4, 5, 6]

def flatten_list(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result
    
# 10. 字典缓存幂函数
# 编写函数power(x, n, cache={})，使用字典缓存优化的幂函数，计算x的n次方

def power(x, n, cache=None):
    if cache == None:
        cache = {}
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n in cache:
        return cache[n]
    else:
        cache[n] = x * power(x, n - 1, cache)
        return cache[n]

# 11. 嵌套字典访问
# 编写函数get_nested_value(data, keys)，从嵌套字典中获取指定键路径的值
# 例如：data={'a':{'b':{'c':1}}}, keys=['a','b','c'] 返回1

def get_nested_value(data, keys):
    for i in keys:
            data = data.get(i)
    return data

# 12. 递归实现组合数
# 编写递归函数combinations(n, k, memo={})，使用字典记忆化计算组合数C(n,k)

def combinations(n, k, memo=None):
    if memo == None:
        memo = {}
    if k == 0 or k == n:
        return 1
    elif k in memo:
        return memo[k]
    else:
        memo[k] = (n - k + 1) / k * combinations(n, k - 1, memo)
        return memo[k]