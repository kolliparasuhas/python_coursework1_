'''
def evenorodd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
n = int(input("enter a number: "))
print(f"{n} is {evenorodd(n)}") 

iseven = lambda n: "even" if n % 2 == 0 else "odd"
print(f"{n} is {iseven(n)}")

l = [1,0,0,0,3,0,4,0,5,0,6,0,3,4,5,6,9,6]
squ =list(filter(lambda i : i != 0,l))
print(f"list after removing zeros: {squ}")

'''
