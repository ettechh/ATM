'''Eric Tech
COMSC230.01
Midterm-1 Program
Goal: Create ATM simulated program with checks and balances, displaying menus '''

#Create variables and ints outside of functions
account_Num = 99999230
password = "0230"
checking_balance = 1000.00
saving_Balance = 1000.00
transactions = []

#function to authenticate user with specific username and password.
def authenticate_user():
        for i in range(3):
            print("Enter a username and password")
            user_account = int(input("Enter your account number: "))
            user_password = input("Enter your password: ")

            if user_account == account_Num and user_password == password:
                print("Welcome User")
                return True
            else:
                print("Incorrect Account Number or Password.")

        return False

#function to display menu for the user to choose 1-5.
def display_Menu():
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Transfer")
    print("4. See Balance")
    print("5. Exit")
    choice = int(input("Enter a number: "))
    return choice

#function for processing a deposit into an account type.
def process_Deposit(checking_balance, savings_balance, transactions):
    user_account_choice = int(input("Choose an account to make a deposit to (1 for Checking, 2 for Savings):  "))

    if user_account_choice == 1:
        deposit_amount = float(input("Enter the amount to deposit into Checking: "))
        if deposit_amount >= 0:
            checking_balance += deposit_amount
            transactions.append(f"Deposit ${deposit_amount} into Checking")
        else:
            print("Deposit must be greater than $0.00")
    elif user_account_choice == 2:
        deposit_amount = float(input("Enter the amount to deposit into Savings: "))
        if deposit_amount >= 0:
            checking_balance += deposit_amount
            transactions.append(f"Deposit ${deposit_amount} into Savings")
        else:
            print("Deposit must be greater than $0.00")

    return checking_balance, savings_balance, transactions


#function to process withdrawal from account types.
def process_Withdrawal(checking_balance, savings_balance, transactions):
    user_account_choice = int(input("Choose an account to make a deposit to (1 for Checking, 2 for Savings):  "))

    if user_account_choice == 1:
        withdrawal_amount = float(input("Enter the amount to withdrawal: "))
        if 0 <= withdrawal_amount <= 400:
            if withdrawal_amount <= checking_balance:
                checking_balance -= withdrawal_amount
                transactions.append(f"Withdrawal ${withdrawal_amount} from Checkings.")
            else:
                print("Insufficient funds in the Checking account.")
        else:
            print("Withdrawal amount must be between $0.00 and $400.00.")

    elif user_account_choice == 2:
        withdrawal_amount = float(input("Enter the amount to withdrawal: "))
        if 0 <= withdrawal_amount <= 400:
            if withdrawal_amount <= savings_balance:
                savings_balance -= withdrawal_amount
                transactions.append(f"Withdrawal ${withdrawal_amount} from Savings.")
            else:
                print("Insufficient funds in the Savings account.")
        else:
            print("Withdrawal amount must be between $0.00 and $400.00.")

    return checking_balance, savings_balance, transactions


#function to process transfers from one account type to another.
def process_transfer(checking_balance, savings_balance, transactions):
    source_account = int(input("Enter a source account type (1 for checking, 2 for savings): "))
    destination_account = int(input("Enter a destination account type (1 for checking, 2 for savings): "))

    if source_account == destination_account:
        print("Account source and destination type can't be the same.")
        return checking_balance, savings_balance, transactions

    source_balance = checking_balance if source_account == 1 else savings_balance
    destination_balance = checking_balance if destination_account == 1 else savings_balance

    transfer_amount = float(input("Enter amount to transfer: "))

    if 0.00 <= transfer_amount <= source_balance:
        source_balance -= transfer_amount
        destination_balance += transfer_amount

        transactions.append(f"Transfer ${transfer_amount} from {source_account} to {destination_account}")
    else:
        print("Invalid transfer amount. Must be between $0.00 and total balance amount.")

    if source_account == 1:
        checking_balance = source_balance
    elif source_account == 2:
        savings_balance = source_balance

    if destination_account == 1:
        checking_balance = destination_balance
    elif destination_account == 2:
        savings_balance = destination_balance

    return checking_balance, savings_balance,transactions

#function to display balance of account types.
def display_balance(checking_balance, saving_Balance, transactions):
    display_choice = int(input("Enter an account to display (1 for checking, 2 for savings): "))

    if display_choice == 1:
        print(checking_balance)
    elif display_choice == 2:
        print(saving_Balance)

    return checking_balance, saving_Balance, transactions


#function to display recent reciepts of the transactions.
def display_receipt(transactions, account_Num):
    print("Recent Transactions: ")
    if not transactions:
        print("No recent transactions.")
    else:
        for index, transaction in enumerate(transactions, start=1):
            print(f"{index}. {transaction}")


#function that calls functions and reads users choice to run the program.
def main():
    authenticated = False
    checking_balance = 1000.00
    savings_balance = 1000.00
    transactions = []

    while not authenticated:
        authenticated = authenticate_user()
        if not authenticated:
            print("Authentication Failed. Try Again.")
    print("Authentication Successful.")

    while True:
        choice = display_Menu()
        if choice == 1:
            checking_balance, savings_balance, transactions = process_Deposit(checking_balance, savings_balance, transactions)
        elif choice == 2:
            checking_balance, savings_balance, transactions = process_Withdrawal(checking_balance, savings_balance, transactions)
        elif choice == 3:
            checking_balance, savings_balance, transactions = process_transfer(checking_balance, savings_balance, transactions)
        elif choice == 4:
            display_balance(checking_balance, savings_balance, transactions)
        elif choice == 5:
            print("Exiting the System...")
            display_receipt(transactions, account_Num)
            break

if __name__ == "__main__":
    main()







