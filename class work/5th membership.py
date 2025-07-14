s='suhas'
print('u' in s) # Check if 'u' is in the string s
print('v' not in s) # Check if 'v' is not in the string s
print('su' in s) # Check if 'su' is in the string s
names= ['suhas', 'sachin', 'siddharth', 'sanjay', 'suresh', 'santosh', 'sagar', 'shubham', 'shreyas', 'shiva']
print('suhas' in names)  # Check if 'suhas' is in the list names
print('sachin' not in names)  # Check if 'sachin'
print('manoj' not in names)
titles =  ['suhas', 'sachin', 'siddharth', 'sanjay', 'suresh', 'santosh', 'sagar', 'shubham', 'shreyas', 'shiva']
a=names
print(id(titles))  # Check if titles and a refer to the same object
print(id(a))  # Check if a and titles refer to the same object
print(id(names))  # Check if names and titles refer to the same object
print(titles is names)  # Check if titles and names are the same object