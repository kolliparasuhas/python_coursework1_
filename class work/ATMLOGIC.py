data = {
    '1234':{'balance': 1000, 'pin': 1234,'history':[]},
    '5678':{'balance': 2000, 'pin': 5678,'history':[]},
    '9101':{'balance': 3000, 'pin': 9101,'history':[]},
    '1122':{'balance': 4000, 'pin': 1122,'history':[]},
    '3344':{'balance': 5000, 'pin': 3344,'history':[]},
    '5566':{'balance': 6000, 'pin': 5566,'history':[]},
}

acc_name = None
login_status = False
def WElcome():
    print("Welcome to the ATM System!".center(40,"-"))
def menu():
    print("ATM Menu".center(40, "-"))
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")
    print("-" * 40)
                               
def login_status(acc,pin):
    if acc in data:
        if data[acc]['pin'] == pin:
            global acc_name
            global login_status
            acc_name = acc
            login_status=True
            print(f"Login successful for account {acc_name}.")
            return True
        else:
            print("Incorrect PIN. Please try again.")
            return False
    else:
        print("Account not found. Please try again.")
        return False
def check_balance():
    if login_status and acc_name:
        print(f"Your current balance is: {data[acc_name]['balance']}")
    else:
        print("Please login first.")

def deposit(amount):
    if login_status and acc_name:
        if amount > 0:
            data[acc_name]['balance'] += amount
            data[acc_name]['history'].append(f"Deposited: {amount}")
            print(f"Deposited {amount}. New balance is: {data[acc_name]['balance']}")
        else:
            print("Deposit amount must be positive.")
    else:
        print("Please login first.")
def withdraw(amount):
    if login_status and acc_name:
        amount = int(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= data[acc_name]['balance']:
            data[acc_name]['balance'] -= amount
            data[acc_name]['history'].append(f"Withdrew: {amount}")
            print(f"Withdrew {amount}. New balance is: {data[acc_name]['balance']}")
        else:
            print("Insufficient funds or invalid amount.")
    else:
        print("Please login first.")
def view_transaction():
    if login_status and acc_name:
        if data[acc_name]['history']:
            print("Transaction history:")
            for transaction in data[acc_name]['history']:
                print(transaction)
        else:
            print("end of transactions found.")