t = (1,2,3,4,5)
t2 = (6,7,8,9)
print(t+t2)  # Concatenates two tuples
print(t*2)  # Repeats the tuple twice
print(t[0:3]*3)  # Slices the tuple and repeats it three times
a,b,c,d,e = t  # Unpacking the tuple
print(a, b, c, d, e)  # Prints unpacked values
tt =(1,2,3,[4,5])
tt[3].append(6)  # Appends 6 to the list inside the tuple
print(tt)  # Prints the modified tuple
