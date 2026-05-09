students=[("Alice",92),("bob",85),("charlie",95)]
sorted_by_grade =sorted(students, key=lambda student:student[1])
print(f"student sorted by grade :{sorted_by_grade}")