s=set()
s={1,2,3,4,5}
print(s)
s.add(6)  # Adds an element to the set
print(s)
class30={'suhas', 'sai', 'siva', 'sanjay', 'saketh', 'smith', 'shiva'}
print(class30)
m1={'suhas', 'sai', 'siva', 'sanjay', 'saketh', 'smith', 'shiva'}
m2={'suhas', 'sai', 'siva', 'sanjay'}
print(m1 | m2)
print(m1 & m2)  # Intersection of two sets
print(m1 - m2)  # Difference of two sets
print(m1 ^ m2)  # Symmetric difference of two sets
print(m1.isdisjoint(m2))  # Checks if two sets are disjoint 
m2.update({'suhas', 'sai', 'siva', 'sanjay'})
