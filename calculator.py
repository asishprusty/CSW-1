
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0 :
        print("second number can not be zero")
    else :
        return a/b
def percentage(a,b):
    return (b/a)*100
def integer_division(a,b):
    return a//b
def power(a,b):
    return a**b
def ceiling(result):
    if result == int(result):
        return result
    else:
        return int(result)+1
def binary(c):
      d=""
      while c>0:
          d=str(c%2)+d
          c=c//2
      return d


def hexadecimal():
    c=ceiling()
    hex_digit="0123456789ABCDEF"
    hex_result=""
    def helper(c):
        while c>0:
            hex_result=hex_result+hex_digit[c%16]
            c=c/16

    return hex_result


       

num1 = float(input("Enter a number: "))
num2 = float (input("Enter another number: "))
op=input("Enter the operator(+,-,*,/,//,**)")
if op=="+":
    r=add(num1,num2)
    print(r)
    user=input("Do you want to convert it to ceiling value(y/n): ")
    if user=="y":
        c=ceiling(r)
        print(c)
    user2=input("Do you want to convert it to binary or hexadecimal(bin/hex): ")
    if user2=="bin":
        print(binary(c))
    if user2=="hex":
        print(hexadecimal(c))
if op=="-":
    r=subtract(num1,num2)
    print(r)
    user=input("Do you want to convert it to ceiling value(y/n): ")
    if user=="y":
        c=ceiling(r)
        print(c)
    user2=input("Do you want to convert it to binary or hexadecimal(bin/hex): ")
    if user2=="bin":
        print=binary(c)
    if user2=="hex":
         print(hexadecimal(c))
if op=="*":
    r=multiply(num1,num2)
    print(r)
    user=input("Do you want to convert it to ceiling value(y/n): ")
    if user=="y":
        c=ceiling(r)
    user2=input("Do you want to convert it to binary or hexadecimal(bin/hex): ")
    if user2=="bin":
        print(binary(c))
    if user2=="hex":
        print(hexadecimal(c))
if op=="/":
    r=divide(num1,num2)
    print(r)
    user=input("Do you want to convert it to ceiling value(y/n): ")
    if user=="y":
        c=ceiling(r)
    user2=input("Do you want to convert it to binary or hexadecimal(bin/hex): ")
    if user2=="bin":
        print(binary(c))
    if user2=="hex":
        print(hexadecimal(c))
if op=="//":
    r=integer_division(num1,num2)
    print(r)
    user=input("Do you want to convert it to ceiling value(y/n): ")
    if user=="y":
        c=ceiling(r)
    user2=input("Do you want to convert it to binary or hexadecimal(bin/hex): ")
    if user2=="bin":
        print(binary(c))
    if user2=="hex":
        print(hexadecimal(c))
if op=="**":
    r=power(num1,num2)
    print(r)
    user=input("Do you want to convert it to ceiling value(y/n): ")
    if user=="y":
        c=ceiling(r)
    user2=input("Do you want to convert it to binary or hexadecimal(bin/hex): ")
    if user2=="bin":
        print(binary(c))
    if user2=="hex":
        print(hexadecimal(c))




