"""data = {
    "suhas99":"123@",
    "suhas123":"1234@",
    "suhas1234":"12345@",}
email,pwd = input("enter username and pwd:").split()
if data.get(email) == pwd:
    print("Login successful")
else:
    print("Login failed")
    print("Please try again")"""




'''
items =['apple', 'banana', 'cherry']
stocks =[10, 5, 20]
data = input ("enter the item to check:")
if data in items :
    print(data,"Item is available")
    ind = items.index(data)
    if stocks[ind]>0:
        print(stocks[ind]," in stock")
    else:
        print("Item is out of stock")
else:
    print(data,"Item is not available")
    print("Please try again")   
# This code checks if a given item is in the list of items and prints appropriate messages.
'''




'''
items=['apple', 'banana', 'cherry']
stocks=[10, 5, 20]
distance=[10,4,6]
rating=[4.5, 3.8, 4.2]
cost=[100, 50, 75]
veg=['yes', 'yes', 'yes']
time=[30, 20, 25]
data = input("Enter the item: ")
ind=items.index(data) 
if distance[ind]<5 and rating[ind]>3 and cost[ind]<500 and veg[ind]=='yes' and time[ind]<30:
    print('filter applied')
elif distance[ind]<5 and rating[ind]>3 and cost[ind]<500 and veg[ind]:
    print('time not matter')
elif distance[ind]<5 and rating[ind]>3 and cost[ind]<500:
    print('veg not matter')
elif distance[ind]<5 and rating[ind]>3:
    print('cost not matter')
elif distance[ind]<5 and rating[ind]>3:
    print('all cost')
elif rating[ind]>3:
    print('distance not matter')
elif distance[ind]<5:
    print('rating not matter')
else:
    print('all items')
    '''



