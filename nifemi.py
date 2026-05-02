def greet():
    print("Hello! Welcome to the world of functions dara")
greet()
greet()
def greet_user(name):
    print(f"good afternoon,{name}!")
greet_user("darasimi")
greet_user("veronica")
greet_user("blessing")
def add_numbers(a,b):
    return a+b
sum_result =add_numbers(5, 3)
print(f"the sum is:{sum_result}")
print(f"the sum of 10 and 20 is:{add_numbers(10,20)}")
print()
def get_power(number, exponent=2):
    return number**exponent
print(f"5 squared is:{get_power(5)}")
print(f"2 to the power of 3 is:{get_power(2,3)}")
print()
def about_me(name,age):
    print(f"my name is {name} my age is {age}")
about_me(age=9, name="sofiyah")
def sum_all(*numbers):
    total=0
    for num in numbers:
        total+=num
    return total
print(f"sum of 1, 2, 3:{sum_all(1, 2, 3)}")
print(f"sum of 10, 20, 30, 40,: {sum_all(10, 20, 30, 40)}")
def display_users_info(**user):
    print("Users information:")
    for key, value in user.items():
        print(f"-{key. title()}: {value}")
display_users_info(name="jane", age=29, city="london")
add_ten= lambda dara: dara + 10
print(f"using lambda: 5+10= {add_ten(5)}")
multpily= lambda a, b: a * b
print(f"using lambda: 3*4= {multpily(3 , 4)})")
points=[(1, 2), (4, 1), (5, -1)]
points.sort(key=lambda point: point[1])
print(f"points sorted by y-cooridnate: {points}")
print()

def multiply_number(number1, number2):
    return number1*number2
print(f"The result is:{multiply_number(9,9)}")


def display_details(first_name, last_name, age):
    print(f"the details are {first_name, last_name, age}")
display_details('mujeedah','darasimi', 13)
def analyze_score():
    5 student, score
score=int(input("enter a number between 1-100"))
if mujeedah score >= 90:
   print(" Grade: A")

