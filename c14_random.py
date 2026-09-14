import random

random_inumber = random.randint(1, 100)  # [1, 100]

random_fnumber = random.uniform(1.0, 100.0)  # [1.0, 100.0)

possibility = random.random()  # [0.0, 1.0)

fruits = ["苹果", "香蕉", "橙子", "葡萄"]
random_fruit = random.choice(fruits)

cards = ["A", "2", "3", "4", "5", "J", "Q", "K"]
random.shuffle(cards)

students = ["小明", "小红", "小刚", "小丽", "小华"]
selected = random.sample(students, 2)

random.seed(42)
print(random.randint(1, 100))
# Fixed No.42 seed. 

# random.choice(x) vs random.sample(x,1):repeated selection vs unique selection