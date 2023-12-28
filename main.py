import random

## Global variables
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

# Dictonary representing symbol-count pairs.
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Dictonary representing symbol-value pairs. 
symbol_value = {
    "A": 10,
    "B": 8,
    "C": 6,
    "D": 4
}

## This function takes in the list of columns, number of lines the user
## would like to bet on, the bet value, and the dictionary representing 
## symbol-value pairs. Each line that is bet on is checked to see if 
## all the values in the row are the same. If they are the same, that
## line is added to winning_lines and the winnings are adjusted 
## accordingly. The winnings and winning_lines are returned.
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    # Loop through the amount of lines that the user picked.
    # If the user picked 2 lines, the top two lines will be 
    # looped through.
    for line in range(lines):
        desired_symbol = columns[0][line]

        # Loop through each column check if the symbol in the column 
        # matches the desired symbol.
        for column in columns:
            symbol = column[line]
            if desired_symbol != symbol:
                break
        # When the for loop doesnt get broken out of, update winnings
        # depending on the value multiplier and add the line number 
        # to winning_lines list.
        else:
            winnings += values[desired_symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
                
## This function takes in a symbol dictionary and the number of rows 
## and columns. The symbol dictionary is looped through and each symbol 
## is added to a comprehensive list. Then each column is looped through,
## and at each row, a randomly generated number is input into the list. 
## Once all columns are looped through and every row has a value, the list
## of column values is returned.
def get_spin(rows, cols, symbols):
    all_symbols = []

    # Loop all items in symbol_count
    for symbol, symbol_count in symbols.items():
        # Loop the count of each symbol and add each symbol 
        # to all_symbols list.
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # Loop all columns and create a copy of all_symbols so that 
    # elements can be removed without changing the original list.
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]

        # Loop all rows in the current column and generate/add a random 
        # value for each.
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        # Add current column to the list of columns
        columns.append(column)

    return columns  

## This function takes in the coulmns with their values and prints them in 
## a proper, readable format. 
def print_spin(columns):
    # Loop through each row
    for row in range(len(columns[0])):

        # Loop through each column and print the value at the current row.
        for i, column in enumerate(columns):
            # Check if last loop is at the last value in the column, and if
            # so, dont add vertical bar for proper formatting 
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")

        print()

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
        lines = input("How many lines would you like to bet on (1 - " + str(MAX_LINES) + ")? ")

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

def spin(balance):
    # Get the number of lines the user would like to bet on.
    lines = get_number_of_lines()

    # Get the amount the user would like to bet and check if they have sufficient funds to 
    # actually bet that amount. Break when the user provide a plausible bet.
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough funds to bet that amount. Your current balance is {balance}")
        else:
            break

    print(f"You are currently betting ${bet} on {lines} lines. Your total bet is equal to ${total_bet}.")

    input("Press any key to spin.") 

    # Get the values for this current spin and print the values.
    spin = get_spin(ROWS, COLS, symbol_count)
    print_spin(spin)

    # Get the winnings and list of winning lines from the spin.
    winnings, winning_lines = check_winnings(spin, lines, bet, symbol_value)

    # Print the users winnings and lines won on.
    print(f"You won ${winnings}")

    if len(winning_lines) == 1:
        print(f"You won on line:", *winning_lines)
    elif len(winning_lines) != 0:
        print(f"You won on lines:", *winning_lines)

    # Return the difference of winnings and the total bet, 
    # representing the gross winning value. This allows balance
    # to be updated correctly.
    return winnings - total_bet
    
def main():
    # Get the initial balance of the user.
    balance = deposit()

    # Game loop.
    while True:
        print(f"Current balance is ${balance}")
        choice = input("Press any key to play (q to quit).")
        if choice == "q":
            break
        balance += spin(balance)

    print(f"You final balance is: {balance}")

main()
