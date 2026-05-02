subject=["maths","biology", "pyhsics"]
for dara in subject:
    print(f"i like {dara}")
for i in range(8):
    add_range=i*8
    print(add_range)
for char in "mujeedah":
    print(char+char+char+char)
student_name="Tomisin"
overall="890"
student_name=input("please enter student_name ")
overall=input("please enter overall ")
if student_name=="tomisin" and overall=="890":
    print("login successful")
else:
   print("invalid login")
score=int(input("enter a number between 1-100"))
if score >= 90:
   print(" Grade: A")
elif score >= 80:
   print(" Grade: B")
elif score >=70:
   print(" Grade: C")
elif score >= 60:
   print(" Grade: D")
elif score >=50:
   print(" Grade: f")
else:
    print(" Grade: e")
for i in range(4, 12, 5):
    print(i)
for index, subject in enumerate(subject):
    print(f"subject at index {index}: {subject}")
count = 4
while count <7:
    print (f"count is {count}")
    count+=7
i=5
while True:
    print(i)
    if i >= 5:
        break
    i+=8
for i in range(4):
    if i == 20: 
        continue
    print(i)
try:
    num_str = '100'
    num=int(num_str)
    print(f"converted number: {num}")
except ValueError:
    print(f"error:could not convert'{num_str}' to an integer")

result=50/5
print(result)
try:
    result=12/2
    print(f"result of division:{result}")
except ZeroDivisionError:
   print(f"error:cannot divide by zero.") 
try:
    value =int(input(" enter number"))
    result = 80/ value
except ValueError:
    print("invalid input. please enter valid integers")
except ZeroDivisionError:
    print("cannot divide by zero.")
except Exception as l:
    print(f"an unexpectederror occurred: {l}")
else:
    print(f"division successful.result: {result}")
finally:
    print("execution of try-execpt block finished.") 