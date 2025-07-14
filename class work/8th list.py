l=[1,2,3,4,5]
l.append(6)
print(l)
tuple_to_list=list((1,2,3,4))
string_to_list =list("suhas")
print(tuple_to_list)
print(string_to_list)
print(string_to_list[0])  # First element
print(string_to_list[1:3])  # Elements from index 1 to 2
print(string_to_list[::-1])  # Elements from index 1 to the end
p=[3,4,6,6,7,8]
p[2]=5
print(p)  # Modified list
print(p.insert(0, 1))
print(sum(l[0:4]))