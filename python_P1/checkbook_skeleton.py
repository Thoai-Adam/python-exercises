import json
import os

#define functions to view balance
def show_balance():
    balance = 0
    
#function to withdraw
def withdraw():

#function to deposit
def deposit():



while True:
    print("welcome to my first checkbook app")
    print("1.view balance")
    print("2.withdraw")
    print("3.deposit")
    print("4.exit")
    #ask for user input
    option = int(input("please enter your option 1-4."))
    #do things
    if option == 1:
        show_balance()
    elif option == 2:
        withdraw()
    elif option == 3:
        deposit()
    elif option == 4:
        exit()
    else:
        print("Go away!")









    with open (your_file, 'w') as f:
        json.dump(balance, f)