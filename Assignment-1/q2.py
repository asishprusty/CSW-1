operation = input("Enter operation (add/sub/mul/div/mod): ")
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))

if operation=="add":
    print(num1+num2)
elif operation=="sub":
    print(num1-num2)
elif operation=="mul":
    print(num1*num2)
elif operation=="div":
    if num2==0:
        print("Division by zero not allowed")
    else:
        print(num1/num2)
elif operation=="mod":
    print(num1%num2)