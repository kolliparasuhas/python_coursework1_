a=12
print(float(a))  # Converts integer to float
print(str(a)) # Converts integer to string
print(complex(a))  # Converts integer to complex number
bool(a)  # Converts integer to boolean
b=12.5
print(int(b))  # Converts float to integer (truncates decimal part)
print(str(b))  # Converts float to string   
print(complex(b))  # Converts float to complex number
bool(b)  # Converts float to boolean
s = 'bunny'
print(list(s))  # Converts string to list of characters
print(tuple(s))  # Converts string to tuple of characters
print(set(s))  # Converts string to set of characters (removes duplicates)
bool(s)  # Converts string to boolean (True if non-empty)
l = ['1', '2', '3']
print(str(l))  # Converts list to string (not recommended for direct conversion)
print(tuple(l))  # Converts list to tuple
print(set(l))  # Converts list to set (removes duplicates)
bool(l)  # Converts list to boolean (True if non-empty)
t = (1, 2, 3)
list(t)  # Converts tuple to list
print(list(t))  # Converts tuple to list 
print(set(t))  # Converts tuple to set (removes duplicates)
print(bool(t))  # Converts tuple to boolean (True if non-empty)
print(str(t))  # Converts tuple to string (not recommended for direct conversion)
a={1,2,3,4}
print(list(a))  # Converts set to list
print(tuple(a))  # Converts set to tuple
print(str(a))  # Converts set to string (not recommended for direct conversion)
print(bool(a))  # Converts set to boolean (True if non-empty)
d = {'a': 1, 'b': 2}
print(list(d))  # Converts dictionary keys to list  
print(tuple(d))  # Converts dictionary keys to tuple
print(str(d))  # Converts dictionary to string (not recommended for direct conversion)
print(bool(d))  # Converts dictionary to boolean (True if non-empty)
print(set(d))  # Converts dictionary keys to set (removes duplicates)