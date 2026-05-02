try:
    num_str="123"
    num=int(num_str)
    print(f"converted number:{num}")
except ValueError:
    print(f"Error coujd not convert'{num_str}' to an interger.")
try:
    value =int(input(" enter number"))
    result = 100/ value
except ValueError:
    print("invalid input. please enter valid integers")
except ZeroDivisionError:
    print("cannot divide by zero.")
except Exception as e:
    print(f"an unexpectederror occurred: {e}")
else:
    print(f"division successful.result: {result}")
finally:
    print("execution of try-execpt block finished.") 
fruits= ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"i like {fruit}")
for char in "python":
    print(char)
for i in range(5):
    print(i)
for i in range(2, 12, 2):
    print(i)
for index, fruit in enumerate(fruits):
    print(f"Fruit at index {index+1}: {fruit}")
count = 0
while count <3:
    print (f"count is {count}")
    count+=1
i=0
while True:
    print(i)
    if i >= 2:
        break
    i+=1
for i in range(5):
    if i == 2: 
        continue
    print(i)
def greet():
    print("Hello! Welcome to the world of functions dara")
greet()
greet()
def greet_user(name):
    print(f"good afternoon,{name}!")
greet_user("darasimi")
greet_user("veronica")