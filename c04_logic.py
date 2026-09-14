door_key = True
password = False
enter_door = door_key and password
point = door_key or password
# print(enter_door)
if enter_door == True:
    print("Welcome inside!")
else:
    print("Access denied!")
if point == True:
    print("One of the conditions is locked.")