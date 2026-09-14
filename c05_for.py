# range()_range(start, stop, step)
Sum = 25
for i in range(1,9,2):
    print(i)
    Sum -= i
print("The final value of Sum is:", Sum)

# Figuring out the answer if range(1,10,2)/range(1,11,2).
# The value of "stop" means the end value but not included.
# The default value of "start" is 0.

Sum = 25
for i in range(1,10,2):
    Sum -= i
print("The final value of Sum is:", Sum)

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

# str & for loop
# Method 1:
word = "iridescent"
indicator = False
for element in range(len(word)):
    print(element)
    if word[element] == "s" or word[element] == "c":
        indicator = True
if indicator:
    print("We found the 's' or 'c' in the word.")
else:
    print("We didnt find the 's' or 'c' in the word.")
# Method 2:
word = "iridescent"
indicator = False
for element in word:
    print(element)
    if element == "s" or element == "c":
        indicator = True
if indicator:
    print("We found the 's' or 'c' in the word.")
else:
    print("We didnt find the 's' or 'c' in the word.")