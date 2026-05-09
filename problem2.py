my_family=["mujeedah","mutteeyah"]
print(my_family[0]) 
my_family.append("sofiyah")
print(my_family)
my_family[0]="barakat"
print(my_family)
regsiter_courses=["maths","english","biology","maths","physics"]
print(f"this is the print out for my  register courses {regsiter_courses}")
unique_courses=set(regsiter_courses)
print("unique courses:",unique_courses)
course_units={}
for course in unique_courses:
    try:
        unit= int(input(f"Enter unit for {course}:"))
        if unit < 1:
            print("unit cannot be less than 1")
        elif unit >= 4:
            print("Heavy course")
            course_units[course] = unit
        elif unit >=2:
            print("normal course")
            course_units[course] = unit
        else:
            print("light course")
            course_units[course] = unit
    except ValueError:
        print("invalid input. please enter a number.")
print("/nFinal course units:")
print(course_units)
add_five= lambda dara: dara + 10
print(f"using lambda: 5+10= {add_five(5)}")


