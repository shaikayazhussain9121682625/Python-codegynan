#Add two numbers
a = int(input())
b = int(input())
print(a + b)
#Quotient and Remainder
a = int(input())
b = int(input())
print("Quotient:", a // b)
print("Remainder:", a % b)
#Even or Odd
n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
#Swap without third variable
a = int(input())
b = int(input())

a = a + b
b = a - b
a = a - b

print(a, b)
#Largest of 3 numbers
a = int(input())
b = int(input())
c = int(input())

print(max(a, b, c))
#Square of a number
n = int(input())
print(n ** 2)
#Divisible or not
a = int(input())
b = int(input())

if a % b == 0:
    print("Divisible")
else:
    print("Not Divisible")
#Area of rectangle
a = int(input())
b = int(input())
print(a * b)
#Positive, Negative, Zero
n = int(input())

if n > 0:
    print("Positive")
elif n == 0:
    print("Zero")
else:
    print("Negative")
    
#Check Eqaul
a = int(input())
b = int(input())

if a == b:
    print("Equal")
else:
    print("Not Equal")
#Condtinal Problems
#Voting elibilty
age = int(input())

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
#Mutiple of 3 nd 5
n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("Yes")
else:
    print("No")
#Greatest of 3 (nested if)
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
        
#Grade
marks = int(input())

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")
#Prime numbers
n = int(input())

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")
    