# user puts amount of bet in
# user pulls lever
# 3 random numbers are generated

# genrate difrent items on the slot machine 
# i don't suport gambling just for fun and utilizing random module

import random


MAX_LINES = 3 # max number of lines to play
MAX_BET = 100 # max bet amount
MIN_BET = 1   # min bet amount

ROWS = 3 # number of rows in slot machine
COLS = 3 # number of columns in slot machine

def Deposit(): 
    # collect user input and return it
    while True:
        try:
            amount = int(input("How much would you like to deposit? $"))
            if amount < 0:
                print("Amount must be greater than 0.")
                pass
            else:
                break
        except ValueError:
            print("Please enter a number")

    return amount

def GetNumberOfLines():
    
    # get number of lines to play
    while True:
        try: 
            lines = int(input("How many lines would you like to bet on? (1-" + str(MAX_LINES) + ")? "))
            if 1 <= lines <= MAX_LINES:
                break                
            else:
                print("Please enter valid number of lines.")
                pass
        except ValueError:
            print("Please enter a number")

    return lines

def GetBetAmount():
    # get bet amount
    while True:
        try: 
            bet = int(input("How much would you like to bet on each line? ($" + str(MIN_BET) + "-$" + str(MAX_BET) + ")? "))
            if MIN_BET <= bet <= MAX_BET:
                break                
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
                pass
        except ValueError:
            print("Please enter a number")

    return bet

def main():
    # main function
    balance = Deposit()
    lines = GetNumberOfLines()
    while True:
        Bet = GetBetAmount()
        TotalBet = Bet * lines
        if TotalBet <= balance:
            break
        else:
            print("You don't have enough money to make that bet. current balance is $", balance, ".100")
            print("Please enter a lower bet amount.")
            pass
        
    print ("You have $", balance, "in your account.")
    print ("You are betting on", lines, "lines.")
    print("you are betting $", Bet, "on each line.")
    print("Your total bet is $", TotalBet, ".")
    
main()