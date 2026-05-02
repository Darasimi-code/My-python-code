num1=int(input("please enter number: "))

if num1%2==0:
  print("even number")
else:
   print("odd number")
score=int(input("enter a number between 1-100"))
if score >= 90:
   print(" Grade: A")
elif score >= 80:
   print(" Grade: B")
elif score >=70:
   print(" Grade: C")
elif score >= 60:
   print(" Grade: D")
else:
   print(" Grade: f")
first_number=int(input("please enter first number "))
second_number=int(input("please enter second number "))
divide=first_number%second_number
print(f"divide({first_number} % {second_number}): {divide}")
password=input("please enter password ")
if len(password) < 6:
   print("password too short")
if len(password) >= 6:
   print("password accepted")
user_name="admin"
password="12345"
user_name=input("please enter user_name ")
password=input("please enter password ")
if user_name=="admin" and password=="12345":
   print("login successful")
else:
   print("invalid login")
student_name=input("please enter student_name")
score=int(input("please enter score"))
number=int(input("please enter number"))