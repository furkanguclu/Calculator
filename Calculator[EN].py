def add(x, y):
    """
    This function adds two numbers.
    
    Parameters:
        x (float): The first number.
        y (float): The second number.
        
    Returns:
        float: The sum of x and y.
    """
    return x + y


def subtract(x, y):
    """
    This function subtracts two numbers.
    
    Parameters:
        x (float): The first number.
        y (float): The second number.
        
    Returns:
        float: The difference between x and y.
    """
    return x - y


def multiply(x, y):
    """
    This function multiplies two numbers.
    
    Parameters:
        x (float): The first number.
        y (float): The second number.
        
    Returns:
        float: The product of x and y.
    """
    return x * y


def divide(x, y):
    """
    This function divides two numbers.
    
    Parameters:
        x (float): The dividend.
        y (float): The divisor.
        
    Returns:
        float: The quotient of the division.
    """
    if y != 0:
        return x / y
    else:
        return "Dividing by zero is not allowed."


while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    operation = int(input("Please select the operation you want to perform: "))

    if operation == 5:
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == 1:
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == 2:
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == 3:
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == 4:
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid operation number. Please try again.")
