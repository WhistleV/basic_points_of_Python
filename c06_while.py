# year = int(input("guess the year of the founding of CUG:"))
# while year != 1952:
#     year = int(input("Wrong guess! Please try it again:"))
# print("Congratulation! U r right!")

year = input("guess the year of the founding of CUG:")
while year != "1952":
    year = input("Wrong guess! Please try it again:")
print("Congratulation! U r right!")

# The difference between int and str input is like upper content.

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