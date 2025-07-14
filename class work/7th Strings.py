
s='howareyoutoday'
s+='hello'
print(s)
print(s[0])  # First character
print(s[1:3])  # Characters from index 1 to 2
print(s[1:])  # Characters from index 1 to the end
print(s[::-1])  # Reversed string
print("you" in s)
print(s.capitalize()) # Capitalizes the first character of the string
print(s.upper())  # Converts the string to uppercase
print(s.lower())  # Converts the string to lowercase        
print(s.count('o'))  # Counts occurrences of 'o'
print(s.title())
print(s.find('o'))  # Finds the first occurrence of 'o'
print(s.startswith("how"))  # Checks if the string starts with "how"
print(s.endswith("llo"))  # Checks if the string ends with "day"   
print(s.isalpha())  # Checks if all characters are alphabetic
print(s.isdigit())  # Checks if all characters are digits
print(s.isalnum())  # Checks if all characters are alphanumeric
rplace = s.replace('o', 'a') # Replaces 'o' with 'a'
print(rplace)  # Prints the modified string
m="hello world"
print(m.split(" "))  # Splits the string into a list of words
print(ord("A"))  # Prints the ASCII value of 'A'
print(chr(65))  # Converts ASCII value 65 back to character 'A'
