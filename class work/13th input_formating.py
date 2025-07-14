name = input("Enter your name: ")
print(type(name))  # Prints the type of the input
#age = input("Enter your age: ")
#print(type(age))  # Prints the type of the input
age = int(input("Enter your age: "))  # Converts input to integer
print(type(age))  # Prints the type of the input
discount = float(input("Enter the discount percentage: "))  # Converts input to float
print(type(discount))  # Prints the type of the input
names = input("Enter names" ).split() # Splits input into a list
print(names)
num=list(map(int, input("Enter numbers: ").split()))  # Converts input to a list of integers
print(num)
num2 = list(map(float, input("Enter numbers: ").split()))  # Converts input to a list of floats
print(num2)
num3 = tuple(map(int, input("Enter numbers: ").split()))  # Converts input to a tuple of integers
print(num3)
num4 = tuple(map(float, input("Enter numbers: ").split()))  # Converts input to a tuple of floats
print(num4)
num5 = set(map(int, input("Enter numbers: ").split()))  # Converts input to a set of integers
print(num5)
num6 = set(map(float, input("Enter numbers: ").split()))  # Converts input to a set of floats
print(num6)
num7 = set(input("Enter numbers: ").split())  # Converts input to a set of strings
print(num7)
num8 = eval(input("Enter an dictionary: "))  # Evaluates the input as a dictionary
print(num8)
user,email,pwd = input("Enter user, email, password: ").split()  # Splits input into three variables
print(user)
print(email)
print(pwd)
