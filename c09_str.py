# get the length of a string
s = "abcdefgh"
print(len(s))

# positive and negative indexing in a string
print(s[0], s[-8])
print(s[4], s[-4])

# slice a string: str[start:stop:step]
print(s[2:6])   # cdef
print(s[2:6:2])    # ce
print(s[6:2:-2])    # ge
print(s[:5])    # abcde
print(s[3:])    # defgh
print(s[3:9])    # defgh
print(s[::])    # abcdefgh = print(s)
print(s[::-1])    # hgfedcba
print(s[::2])    # aceg
# figure out the pattern of slicing_s[start:stop:step]
# slice out of the object doesnt output Error!!!

word = "park"
word = "b" + word[1:]
print(word)   # bark
word = word[:3] + "e"
print(word)   # bare

s1 = 'hello, world!'
# 字符串首字母大写
print(s1.capitalize())  # Hello, world!
# 字符串每个单词首字母大写
print(s1.title())       # Hello, World!
# 字符串变大写
print(s1.upper())       # HELLO, WORLD!
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())       # goodbye