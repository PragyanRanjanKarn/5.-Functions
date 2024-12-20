
# 1. First Program
def f1():
    name=input("Enter your name : ")
    print("Hello", name)
f1() # Function Calling / Invoking

# 2. Second Program
def f2(a, b): #a, b are parameters
    c = a + b 
    print("Addition = ", c)
    c = a - b 
    print("Subtraction = ", c)
    c = a * b 
    print("Multiplication = ", c)
    c = a / b 
    print("Division = ", c)
    c = a // b 
    print("Floor Division = ", c)
    c = a ** b 
    print("Exponent = ", c)
    c = a % b 
    print("Modulus = ", c)

n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second number :"))
n3 = int(input("Enter Third number :"))

f2(n1, n2)

# 3. Third Program
def f3(a, b, c) :
    return a*b*c
print("Multiplication of ", n1, n2, n3, "=", f3(n1, n2, n3))

# 4. n = 5 -> n! -> 5! -> 1 * 2 * 3 * 4 * 5 = 120

n = int(input("Enter your number : "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i # fact = 1 * 1 = 1, fact = 1 * 2 = 2, fact = 2 * 3 = 6, fact = 6 * 4= 24, fact = 24 * 5 = 120
print("Factorial of " , n, "is" , fact)




