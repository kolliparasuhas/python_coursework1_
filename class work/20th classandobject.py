'''
class number:
    a = 10
    def update(self,number):
        self.b = number
n1 = number()
'''
'''
class shopping:
    discount = 10
    @classmethod
    def update(cls,new_discount):
        cls.discount = new_discount
        print(f'{new_discount} is updated')

    def product (self,price,name):
        self.price = price
        self.name = name
    @staticmethod
    def check(price):
            print('$%.2f'% price)
user1 = shopping()
user1.product(100000, "laptop")
user2 = shopping()
user2.product(25000, "mobile")

print(shopping.products)
shopping.update(20)
print(user1.price)
user1.price = user1.price - (user1.price * shopping.discount / 100)
print(user1.price,"after discount")
'''

class login:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.followers =[]
        self.accountstatus = False
        self.bio = ""
        self.post =[]
    def updatepassword(self, new_password):
        self.password = new_password
    def display(self):
        print(f"{self.name}'s password is: {self.password}")
    def updatebio(self,bio):
        self.bio = bio

dinesh=login("dinesh","1234")
sanjay=login("sanjay","5678")
dinesh.display()
sanjay.display()
dinesh.updatepassword("abcd")
dinesh.display()