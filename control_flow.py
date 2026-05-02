fruits=["apple","banana", "cherry"]
for dara in fruits:
    print(f"i like {dara}")
for char in "python":
    print(char+char)
#for i in range(5):
#    multiply_range=i*2
#    print(multiply_range)
for i in range(2, 10, 2):
    print(i)
for index, fruit in enumerate(fruits):
    print(f"Fruit at index {index}: {fruit}")
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
