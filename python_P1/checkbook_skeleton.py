import json
import os
balance = 0
#define functions to view balance
def show_balance(value):
    print(value)

#function to withdraw
def withdraw(bal):
    withdraw_amount = int(input("what would you like to withdrawl: "))
    return bal - withdraw_amount

#function to deposit
def deposit(bal):
    deposit_amount = int(input("what would you like to deposit: "))
    return bal + deposit_amount
    
your_file = 'checkbook.json'
def write_balance_to_file(balance):
    with open (your_file, 'w') as f:
        json.dump(balance, f)

while True:
    print("Welcome to my first checkbook app")
    print("1.view balance")
    print("2.withdraw")
    print("3.deposit")
    print("4.exit")
    #ask for user input
    option = int(input("please enter your option 1-4."))
    #do things
    if option == 1:
        show_balance(balance)
    elif option == 2:
        balance = withdraw(balance)   #because my function has a return statement 
    elif option == 3:
        balance = deposit(balance)
    elif option == 4:
        write_balance_to_file(balance)
        break
    else:
        continue