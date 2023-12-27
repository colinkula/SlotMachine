'''
Text based slot machine

1. Let the user deposit money 
2. Allow the user to bet on 1, 2, or 3 lines on the slot machine
3. Determine if the user won
    multiply the users bet by the value of the line, add it to their balance, and allow them to continue playing

'''
## Global variables
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

## Take in user input for a specified deposit amount and return that value.
def deposit():
    # Enter valid amount of money 
    # Loop until user correctly enters number
    while True:
        amount = input("How much would you like to deposit? $")

        # Check that the amount is a viable number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


## Take in user input for a specified number of lines and return that value.
def get_number_of_lines():
    # Enter valid number of lines     
    # Loop until user correctly enters number
    while True:
        lines = input("Enter the number of lines you would like to bet on.\n"
            + "Select a number in the following range (1 - " + str(MAX_LINES) + ") ")

        # Check that the number of lines is a viable number
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("The number of lines must be within the following range (1 - "
                    + str(MAX_LINES) + ")")
        else:
            print("Please enter a number.")

    return lines


## Take in user input for the specified amount they would like to bet and return that value. 
def get_bet():
    # Enter valid bet amount     
    # Loop until user correctly enters number
    while True:
        bet = input("How much would you like to bet for each line? $")

        # Check that the bet is a viable number
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"The bet must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")

    return bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough funds to bet that amount. Your current balance is {balance}")
        else:
            break

    print(f"You are currently betting ${bet} on {lines} lines. Your total bet is equal to ${total_bet}.")


main()
