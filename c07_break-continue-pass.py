# break in while loop
sum = 0
i = 5
while i < 11:
    sum += i
    i += 2
    if sum == 5:
        break
print(sum)

# break in for loop
sum = 0
for i in range(5,11,2):
    sum += i
    if sum == 5:
        break
print(sum)

def process_student_grades(grades):
    valid_grades = []
    for grade in grades:
        if grade < 0 or grade > 100:
            print(f"{grade} is invalid.")
            continue
        if grade >= 90:
            level = 'A'
        elif grade >= 80:
            level = 'B'
        elif grade >= 70:
            level = 'C'
        elif grade >= 60:
            level = 'D'
        else:
            level = 'F'
        valid_grades.append((grade, level))
    return valid_grades

class DatabaseConnector:
    def connect(self):
        pass
    def disconnect(self):
        pass
    def execute_query(self, sql):
        pass
    def fetch_all(self):
        pass