'''
for j in range(5):
    for i in range(3):
        print(i,end =" ")
    print()

for row in range(5):
    for col in range(5):
        print("*",end=" ")
    print()

for i in range(5):
    for j in range(5):
        print(j, end=" ")
    print()

for j in range(5):
    for i in range(5):
        print(j, end=" ")
    print()

for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()

for i in range(5,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()

for i in range(5):
    for col in range(5-i-1):
        print(' ', end=' ')
    for col1 in range(i+1):
        print('*',end=' ')
    print()

for i in range(5):
    for col in range(i):
        print(' ', end=' ')
    for col1 in range(5-i):
        print('*',end=' ')
    print()


#to create a hallow square
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


n=int(input("Enter the size of the square: "))   
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == n//2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
      
n=int(input("Enter the size of the square: "))   
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i+j ==(n-1) :
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

n = int(input("Enter the size of the square: "))
for i in range(n):
    for j in range(n):
        if i == i or i == i-1 or j == j or j == j-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

    
n = int(input("Enter the size of the square: "))
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()




#print a letter "G" with stars
n = int(input("Enter the size of the letter G: "))
for i in range(n):
    for j in range(n):
        if (i == 0 and j < n-1) or (j == 0 and i > 0 and i < n-1) or (i == n-1 and j < n-1) or (j == n-1 and i >= n//2) or (i == n//2 and j >= n//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


# Print a letter "R" with stars
n = int(input("Enter the size of the letter R: "))
for i in range(n):
    for j in range(n):
        if (j == 0) or (i == 0 and j < n-1) or (i == n//2 and j < n-1)  or (j == n-1 and i < n//2) or (i == 1 and j == n-1) or (i == j and i > n//2) :
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


# Print a letter "M" with stars
n = int(input("Enter the size of the letter M: "))
for i in range(n): 
    for j in range(n):
        if  (j == 0) or (j == n-1)  or(i == j and i < n//2) or (i + j == n - 1 and i < n//2) or (i == n//2 and j== n//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

'''
n = int(input("Enter the size of the letter K: "))
for i in range (n):
    for j in range (n):
        if (j == 0) or (i +j == n-1 and i <= n//2) or (i - j == 0 and i >= n//2) or (i == n//2 and j < n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    