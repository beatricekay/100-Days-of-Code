import art

# This version 2 includes:
# 1) The repeating steps outside the IF loop
# 2) Recursion

##Calculator Functions
#Add
def add(n1, n2):
    return n1 + n2

#Subtract second number from first number
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide first number by second number
def divide(n1, n2):
    return n1 / n2

##Operations Dictionary - to call the functions depending on which operation is chosen
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)

    # First number
    num1 = float(input("What's the first number?: "))

    # Print out all the symbols for the user to choose 
    for symbol in operations: 
        print(symbol)

    # Method 2 does not need this to be defined
    # user_choice = "y" 
    continue_calculation = True

    # Method 2: Actions are outside the if loop
    while continue_calculation == True:

        # Select an operation
        operation_symbol = input("Pick an operation: ")

        # Next number
        num2 = float(input("What's the next number?: "))

        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Check if user wants to continue the calculation
        user_choice = input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation: ")

        if user_choice == "y":
            continue_calculation = True
            # Update num1 to be the latest answer
            num1 = answer

        elif user_choice == "n":
            continue_calculation = False
            calculator() # recursion

# Call the function with recursion
calculator()