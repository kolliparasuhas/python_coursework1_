d={'name': 'suhas','age':23,'city':'hyd'}
d.get('name')  # Returns the value for the key 'name'
print(d['name'] ) # Accesses the value for the key 'name'
print(d.get('name'))  # Returns the value for the key 'name'
print(d.get('country', 'India'))  # Returns 'India' if 'country' key is not found
#print(d.pop('age'))
#d.clear()  # Clears the dictionary
print(d.keys())  # Returns a view of the dictionary's keys
print(d.values())  # Returns a view of the dictionary's values  
print(d.items())  # Returns a view of the dictionary's items (key-value pairs)
d['country'] = 'India'  # Adds a new key-value pair to the dictionary
d.get('batch','bathch is not found')  # Returns 'bathch is not found' if 'batch' key is not found
d.setdefault('batch', 'python')  # Sets default value for 'batch' key if not present
print(d)  # Prints the updated dictionary
print(len(d))
print(max(d))
print(min(d))  # Returns the minimum key in the dictionary
print(sorted(d))  # Returns a sorted list of the dictionary's keys
