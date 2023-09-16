# user puts amount of bet in
# user pulls lever
# 3 random numbers are generated

# genrate difrent items on the slot machine 
# i don't suport gambling just for fun and utilizing random module

MAX_LINES = 3 # max number of lines to play

def deposit(): 
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
            lines = int(input("How many lines would you like to bet on? "))
            if lines < 0:
                print("Amount must be greater than 0.")
                pass
            else:
                break
        except ValueError:
            print("Please enter a number")

    return lines

def main():
    # main function
    # print("Welcome to the slot machine!")
    # print("You have $", deposit(), "in your account.")
    balance = deposit()
    
main()