numbers=[]
while True:
    num= input("Enter a number (or 'done'): ")
    if num=="done":
        break
    numbers.append(float(num))
numbers.sort()
print("Sorted: ", numbers)