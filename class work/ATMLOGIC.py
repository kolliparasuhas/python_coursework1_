data = {
    '1234':{'balance': 1000, 'pin': 1234,'history':[]},
    '5678':{'balance': 2000, 'pin': 5678,'history':[]},
    '9101':{'balance': 3000, 'pin': 9101,'history':[]},
    '1122':{'balance': 4000, 'pin': 1122,'history':[]},
    '3344':{'balance': 5000, 'pin': 3344,'history':[]},
    '5566':{'balance': 6000, 'pin': 5566,'history':[]},
}

acc_name = None
def login(acc,pin):
    if acc in data:
        if data[acc]['pin'] == pin:
            global acc_name
            acc_name = acc
            print(f"Login successful for account {acc_name}.")
        else:
            print("Incorrect PIN. Please try again.")
    else:
        print("Account not found. Please try again.")
def check_balance():
    if login_status():
        print(f"Your current balance is: {data[acc_name]['balance']}")
    else:
        print("Please login first.")

def deposit(amount):
    if login_status():
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
            print("No transactions found.")