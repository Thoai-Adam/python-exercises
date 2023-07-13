import json
import os



def welcome_message():
    print("~~~ Welcome to your terminal checkbook! ~~~")
    
def main():
    welcome_message()

    while True:
        print("\nWhat would you like to do?")
        print("1. View current balance")
        print("2. record a debit (withdrawal)")
        print("3. record a credit (deposit)")
        print("4. exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_balance()
        elif choice == "2":
            add_debit()
        elif choice == "3":
            add_credit()
        elif choice == "4":
            exit_application()
        else:
            print('Go Away!')

def get_balance():
    balance = 0
    if os.path.exists("transactions.txt"):
        with open("transactions.txt", "r") as file:
            for line in file:
                transaction_type, amount = line.split()
                if transaction_type == "credit":
                    balance += float(amount)
                elif transaction_type == "debit":
                    balance -= float(amount)
    return balance


def view_balance():
    balance = get_balance()
    print(f"view current balance: {balance}")


def add_debit():
    amount = float(input("Enter the debit amount: "))
    with open("transactions.txt", "a") as file:
        file.write(f"User deposited {amount}\n")
    print("Debit added successfully.")


def add_credit():
    amount = float(input("Enter the credit amount: "))
    with open("transactions.txt", "a") as file:
        file.write(f"User withdrawled {amount}\n")
    print("Credit added successfully.")


def exit_application(): 
    print("Exiting the Banking Application.") 
    exit()

if __name__ == "__main__":
    main()
