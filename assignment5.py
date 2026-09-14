# 对下列函数作列表生成式的优化：
# 1.  nums1 = [35, 12, 97, 64, 55]
#     nums2 = []
#     for num in nums1:
#         nums2.append(num ** 2)
#     print(nums2)
# 2.  nums1 = [35, 12, 97, 64, 55]
#     nums2 = []
#     for num in nums1:
#         if num > 50:
#             nums2.append(num)
#     print(nums2)

nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)

nums1 = [35, 12, 97, 64, 55]
nums2 = [num for num in nums1 if num > 50]
print(nums2)

# 1.1 创建一个元组，包含你的姓名、年龄、身高（米）和所在城市，并打印输出
# 1.2 访问并打印元组中的第一个和最后一个元素
# 1.3 尝试修改元组中的一个元素（观察错误信息），理解元组的不可变性
# 1.4 元组解包：将上述元组中的每个元素分别赋值给不同的变量，并打印这些变量
# 1.5 创建一个空元组和一个只包含一个元素的元组（注意语法）

info = ('WhistleV_', 18, 1.75, 'Wuhan')
print(info[0], info[-1])
info[0] = 'Rz.'  # Invalid: (TypeError) tuple is invariable.
name, age, height, city = info
print(name, age, height, city)
tuple_empty = []; tuple_one = ['x',]

# 2.1 创建两个元组，分别包含一些数字，然后将它们连接起来形成一个新的元组
# 2.2 使用切片操作获取新元组中的第2到第4个元素（包含第2和第4）
# 2.3 编写一个函数，接收一个元组参数，返回该元组的倒序元组（使用切片）
# 2.4 利用元组交换两个变量的值

tuple_1 = (33, 45, 65)
tuple_2 = (87, 26, 23)
tuple_2 += tuple_1
tuple_2[1:4]
def reverse_tuple():
    a_tuple = input("Enter datas, separate with commas: ")
    return a_tuple[::-1]
print(reverse_tuple)
x = 9; y = 1
x, y = y, x
print(x, y)

# 3.1 编写一个函数，接收两个数字参数，返回它们的和、差、积、商（整数除）和余数（使用元组返回多个值）
# 3.2 调用该函数，并使用元组解包接收所有返回值
# 3.3 仿照课件中的例子，编写函数 get_data()，统计以下元组中数字的最小值、最大值和不重复单词的个数
# test_data = ((1, "apple"), (3, "banana"), (2, "apple"), (5, "orange"), (4, "banana"))
# 期望输出：最小值1，最大值5，不重复单词数3（apple, banana, orange）

def calculate():
    x = float(input("Enter a number: "))
    y = float(input("Enter the next number: "))
    sum = x + y
    dfr = x - y
    prd = x * y
    iquo = x // y
    rem = x % y
    temp_tuple = sum, dfr, prd, iquo, rem
    return temp_tuple 
summar, difference, product, int_quotient, remainder = calculate()
print(summar, difference, product, int_quotient, remainder)
def get_data(aTuple):
    nums = ()
    words = ()
    for x in aTuple:
        nums += (x[0],)
        if x[1] not in words:
            words += (x[1],)
    temp_max = max(nums)
    temp_min = min(nums)
    temp_unique_words_amount = len(words)
    return temp_max, temp_min, temp_unique_words_amount
test_data = ((1, "apple"), (3, "banana"), (2, "apple"), (5, "orange"), (4, "banana"))
max, min, unique_words_amount = get_data(test_data)
print(f"The maximum of the data is {max}, the minimum of the data is {min}, the amount of the unique words is {unique_words_amount}.") 

# 4.1 创建一个列表，包含5种你最喜欢的水果名称
# 4.2 使用索引访问并打印列表中的第一个和最后一个水果
# 4.3 修改列表中的第二个元素为另一种水果，并打印列表以观察变化
# 4.4 使用 append() 方法在列表末尾添加一种新的水果
# 4.5 使用 insert() 方法在列表的第三个位置插入一种水果
# 4.6 使用 del 语句删除列表中的第一个元素

lst = ['apple', 'orange', 'watermelon', 'grape', 'hamimelon']
print(lst[lst.index('apple')], lst[lst.index('hamimelon')])
lst[1] = 'mango'
print(lst)
lst.append('pear')
lst.insert(2,'strawberry')
del lst[0]
print(lst)

# 5.1 创建一个包含一些重复元素的列表，例如：[1, 2, 3, 2, 4, 2, 5]
# 5.2 使用 count() 方法统计数字2在列表中出现的次数
# 5.3 使用 index() 方法找到数字4在列表中的索引位置
# 5.4 使用 remove() 方法删除第一个出现的数字2
# 5.5 使用 pop() 方法删除并返回列表的最后一个元素，并打印返回值
# 5.6 使用 sort() 方法对列表进行升序排序（注意：sort() 是原地排序）
# 5.7 使用 sorted() 函数对列表进行降序排序（不改变原列表），并打印新列表

lst = [1, 2, 3, 2, 4, 2, 5]
print(lst.count(2))
print(lst.index(4))
lst.remove(2)
a = lst.pop(-1)
print(a)
lst.sort()
print(lst)
lst2 = sorted(lst)
print(lst2)

# 6.1 将字符串 "Hello, World!" 转换成列表，每个字符作为一个元素
# 6.2 将字符串 "apple,banana,orange,grape" 以逗号为分隔符拆分成列表
# 6.3 有一个包含单词的列表：['Python', 'is', 'fun']，用空格将列表元素连接成一个字符串
# 6.4 有一个包含数字的列表：[1, 2, 3, 4, 5]，用连字符 '-' 将它们连接成一个字符串（注意先将数字转换为字符串）

lst1 = list("Hello, World!")
lst2 = "apple,banana,orange,grape".split(',')
lst3 = ['Python', 'is', 'fun']
str1 = " ".join(lst3)
lst4 = [1, 2, 3, 4, 5]
lst4_str = [str(t) for t in lst4]
str2 = "-".join(lst4_str)
print(lst1, lst2, str1, str2)

# 7.1 创建两个列表 L1 和 L2，将 L1 赋值给 L2（即创建别名），修改 L2 的一个元素，观察 L1 是否变化
# 7.2 使用切片克隆 L1 得到 L3，修改 L3 的一个元素，观察 L1 是否变化
# 7.3 创建一个嵌套列表（列表中的元素也是列表），例如：list1 = [1, [2, 3], 4]
#     将 list1 赋值给 list2（别名），然后修改 list2 中嵌套列表的元素，观察 list1 的变化
#     再用切片克隆 list1 得到 list3，修改 list3 中嵌套列表的元素，观察 list1 是否变化？
#     思考：为什么切片克隆对于嵌套列表不能完全独立？如何实现深拷贝？（可选，可以使用 copy 模块的 deepcopy）

L1 = [1, 2, 3, 4]
L2 = L1
del L2[-1]
L2.append(3)
print(L1, L2)
L3 = L1[:]
del L3[-1]
L3.append(4)
print(L1, L3)
list1 = [1, [2, 3], 4]
list2 = list1
del list2[-1]
list2.append(3)
print(list1,list2)
list3 = list1[:]
del list3[-1]
list3.append(5)
print(list1, list3)
list4 = list1[:]
list4[2][1] = 100
print(list1, list4)
# 切片克隆（浅拷贝）会在新列表中复制原列表的所有元素的引用。这意味着：
#     对于不可变类型（如整数、字符串、元组等）：修改这些元素不会影响原列表，因为实际上你是在新列表中替换了引用。
#     对于可变类型（如列表、字典等）：嵌套的可变对象仍然是同一个对象，所以通过新列表修改嵌套可变对象的元素，原列表也会被修改。

# 8.1 编写一个函数，接收一个列表参数，在函数内部修改该列表（例如，将每个元素加1）
# 8.2 编写一个函数，接收一个列表参数，返回一个新的列表，新列表中的元素是原列表每个元素的平方，原列表不变。

test_data_tuple = (1, 4, 8)
def modify_each_elem_add1(aTuple1):
    aTuple1_list = list(aTuple1)
    for i in range(len(aTuple1_list)):
        aTuple1_list[i] += 1
    return tuple(aTuple1_list)
def modify_each_elem_square(aTuple2):
    aTuple2_list = list(aTuple2)
    for j in range(len(aTuple2_list)):
        aTuple2_list[j] = aTuple2_list[j] ** 2
    return tuple(aTuple2_list) 
print(modify_each_elem_add1(test_data_tuple), modify_each_elem_square(test_data_tuple))

# 9.1 编写一个函数，接收一个列表，返回一个新的列表，新列表包含原列表中的所有不重复元素（顺序可以打乱）
# 9.2 编写一个函数，接收一个列表，返回一个新的列表，新列表是原列表的倒序（不能使用 reverse() 或切片，使用循环实现）
# 9.3 编写一个函数，接收两个列表，返回两个列表的交集（即两个列表中都有的元素）列表，要求结果中每个元素只出现一次
#     例如：list1 = [1, 2, 2, 3, 4], list2 = [2, 3, 5]，则返回 [2, 3]

def f1():
    lst1_str = input("Enter elements, separate with commas: ")
    lst1 = [x for x in lst1_str.split(',')]
    lst11 = []
    for i in lst1:
        if i not in lst11:
            lst11.append(i)
            lst1.remove(i)
    for j in lst11:
        if j in lst1:
            lst11.remove(j)
        return lst11
print(f1())
def f2():
    lst2_str = input("Enter elements, separate with commas: ")
    lst2 = [x for x in lst2_str.split(',')]
    lst22 = []
    for k in lst2:
        lst22.insert(0, k)
    return lst22
print(f2())
def f3():
    lst3_str = input("Enter the first set of elements, separate with commas: ")
    lst4_str = input("Enter the second set of elements, separate with commas: ")
    lst3, lst4 = [x for x in lst3_str.split(',')], [x for x in lst4_str.split(',')]
    lst33 = []; lst44 = []
    for l in lst3:
        if l in lst4:
            lst33.append(l)
    for u in lst33:
        if u not in lst44:
            lst44.append(u)
    return lst44
print(f3())

# 10.1 使用嵌套列表表示一个3x3的矩阵，例如：[[1,2,3],[4,5,6],[7,8,9]]
# 10.2 编写函数打印矩阵（每行一行）
# 10.3 编写函数计算矩阵的转置（行列互换）
# 10.4 编写函数计算两个矩阵的加法（假设两个矩阵维度相同）

Matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
Matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
def print_Matrix(Matrix1):
    for i in Matrix1:
        print(i)
def transposed_Matrix(Matrix1):
    Matrix11 = []
    for i in range(3):
        new_rows = []
        for j in range(3):
            new_rows.append(Matrix1[j][i])
        Matrix11.append(new_rows)
    print_Matrix(Matrix11)
    return Matrix1
def add_Matrix(Matrix1, Matrix2):
    sum = []
    for i in range(3):
        new_rows1 = []
        new_rows1 = [Matrix1[i][j] + Matrix2[i][j] for j in range(3)]
        sum.append(new_rows1)
    print_Matrix(sum)
    return sum
print_Matrix(Matrix1)
print(transposed_Matrix(Matrix1))
print(add_Matrix(Matrix1, Matrix2))