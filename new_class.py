try:
    num_str = '10'
    num=int(num_str)
    print(f"converted number: {num}")
except ValueError:
    print(f"error:could not convert'{num_str}' to an integer")

result=10/2
print(result)
try:
    result=10/2
    print(f"result of division:{result}")
except ZeroDivisionError:
   print(f"error:cannot divide by zero.") 
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
 