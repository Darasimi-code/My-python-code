temperature = 5

#if temperature > 20:
    #print("it's a warm day.")
    
#if temperature < 10:
    #print("it's cold.")
#else:
    #print("it'not cold.") 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
score=int(input("please enter score "))
if score>=90:
    print(" Grade: A")
elif score >= 80:
    print(" Grade: B")
elif score >=70:
    print(" Grade: C")
else:
    print(" Grade: f")
age =10
has_license =False
if age>= 18:
    if has_license:
        print("you can drive")
    else:
        print("you are old enough, but need a license to drive")
else:
    print("you are too young to drive")  
lang =input("what's the programming language you want to learn ")

#SWITCH CASE
"""
match lang:
    case "javascript":
        print("you can become a web developer")
    case "python":
       print("you can be a data scientist ")
    case "PHP":
        print("you can become a backend developer") 
    case "solidity":
        print("you can become a blockchain developer")
    case "java":
        print("you can become a mobil app developer")
    case _:
        print("the language does not matter. what matter is solving problems.")
"""

#IF_ELIF_ELSE
if lang == "javascript":
    print("you can become a web developer")
elif lang =="python":
    print("you can be a data scientist ") 
elif lang == "PHP":
    print("you can become a backend developer") 
elif lang == "solidity":
    print("you can become a blockchain developer")
elif lang == "java":
    print("you can become a mobil app developer") 
else:
    print("the language does not matter. what matter is solving problems.")

