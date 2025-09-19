age = int(input("Enter your age: "))

# Run the if-else to check whether the user is an adult or minor
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Run the while loop independently, regardless of the age
count = 1
while count <= 5:
    print(count)
    count += 1
