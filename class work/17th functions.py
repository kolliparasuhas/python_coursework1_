'''
def wish(name,batch=30):
    print(f"welcome to python {name} and batch {batch}!!!")
name = input("enter name: ")
wish(name)

def update(n):
    print(f"before update: {n}")
    k =n
    k.append(20)
    print(f"after update: {n}")
n=[1,2,3]
update(n)
print("outside of function:",n)

def sumofnum(n):
    if n==0:
        return 0
    return n+sumofnum(n-1)
n=int(input("enter a number: "))
print(f"sum of numbers from 1 to {n} is: {sumofnum(n)}")

def factorial(n):
    if n ==1:
        return 1
    return n* factorial(n-1)
n = int(input("enter a number: "))
print(f"factorial of {n} is: {factorial(n)}")


def shoot(n):
    if n == 0:
        return 0
    print("before recurtion shoot:", n)
    shoot(n - 1)
    print("after recurtion shoot:", n)
n = int(input("enter a number: "))
shoot(n)

'''
# Fibonacci series using recursion
n = int(input("enter a number: "))
a =0
b=1
if n == 1:
    print(a)
elif n >= 2:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c
else:
    print("please enter a valid number greater than 0")