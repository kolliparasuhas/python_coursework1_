import ATMLOGIC 
acc = input("Enter your account number: ")
pin = int(input("Enter your PIN: "))

ATMLOGIC.WElcome()

if ATMLOGIC.login_status(acc, pin):
    while True:
        ATMLOGIC.menu()
        op = int(input("Select an option: "))
        if op == 1:
            ATMLOGIC.check_balance()
        elif op == 2:
            amount = float(input("Enter amount to deposit: "))
            ATMLOGIC.deposit(amount)
        elif op == 3:
            ATMLOGIC.withdraw(amount)
        elif op == 4:
            ATMLOGIC.view_transaction()
        elif op == 5:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            break
