'''
name = 'suhas'
for ch in name:
    print(f"ch = {ch}")

'''
'''
name = ['suhas', 'sai', 'bunny']
for ch in name:
    print(f"ch = {ch}") 

'''
'''
name = {'suhas', 'sai', 'bunny'}
for ch in name:
    print(f"ch = {ch}") 

'''
'''
name={1:'dinesh',2:'gopal',3:'suhas',4:'shivani'}
for i in name.keys():
    print(f'{i}- {name[i]}')
'''
'''
name={1:'dinesh',2:'gopal',3:'suhas',4:'shivani'}
for i in name.keys():
    print(f'{i}- {name[i].title()}')
'''
'''
a = 10
for i in range(1,a+1):
    print(f"{i} - {i*i}")
'''
email = 'asd@123'
pwd = '123@'
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    user_email = input("Enter email: ")
    user_pwd = input("Enter password: ")
    if user_email == email and user_pwd == pwd:
        print("Login successful")
        break
    else:
        attempts += 1
        print("Login failed")
        
else:
    print("Maximum attempts reached. Please try again later.")