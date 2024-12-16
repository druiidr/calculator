TAYLOR_SERIES_REPETITIONS=30


def factorial(num):
    """
    Returns the factorial of a non-negative integer.
    
    Args:
        num (int): The number to factorialize.
        
    Returns:
        int: The factorial of the input number.
        
    Raises:
        ValueError: If the input is a negative number.
    """
    if num < 0 or type(num)!=int:
        raise ValueError("Attempted to factorialize a non-integer.")
    if num == 0:
        return 1
    return num * factorial(num - 1)

def digitSum(num):
    """
    Returns the sum of the digits of a given number.
    
    Args:
        num (float): The number to sum.
        
    Returns:
      int: sum of the digits of the input number..
     """
    num_str = str(num).replace('.', '')
    num = sum(int(digit) for digit in num_str)
    
    return num

def taylorLn(x):
    """
    Approximates ln(x) using a Taylor series expansion.

    Args:
        x (float): The number to compute the natural logarithm for (x > 0).
        
    Returns:
        float: The approximate value of ln(x).
        
    Raises:
        ValueError: If x <= 0 since ln(x) is undefined for non-positive values.
    """
    if x <= 0:
        raise ValueError("ln(x) is undefined for x <= 0")
    
    # Transformation to improve convergence
    numerator = (x - 1)
    denominator = (x + 1)
    fraction = numerator / denominator

    total = 0
    for n in range(2*TAYLOR_SERIES_REPETITIONS):
        term = (1 / (2 * n + 1)) * (fraction ** (2 * n + 1))
        total += term

    return 2 * total

def taylorSine(num):
    """
    Approximates sin(x) using the Taylor series expansion.
    
    Args:
        num (float): The angle in radians.
        
    Returns:
        float: The approximate value of sin(x).
    """
    total = 0
    for i in range(TAYLOR_SERIES_REPETITIONS):
        term = ((-1)**i * num**(2 * i + 1)) / factorial(2 * i + 1)
        total += term
    return total


def taylorCosine(num):
    """
    Approximates cos(x) using the Taylor series expansion.
    
    Args:
        num (float): The angle in radians.
        
    Returns:
        float: The approximate value of cos(x).
    """
    total = 0
    for i in range(TAYLOR_SERIES_REPETITIONS):
        term = ((-1)**i * num**(2 * i)) / factorial(2 * i)
        total += term
    return total


def tangent(num):
    """
    Approximates tan(x) using the ratio of sine and cosine.
    
    Args:
        num (float): The angle in radians.
        
    Returns:
        float: The approximate value of tan(x).
    """
    return taylorSine(num) / taylorCosine(num)


def maximal(num1, num2):
    """
    Returns the larger of two numbers.
    
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        
    Returns:
        float: The larger of the two numbers.
    """
    return num1 if num1 > num2 else num2


def negate(operand):
    """
    Negates the input number.
    
    Args:
        operand (float): The number to negate.
        
    Returns:
        float: The negated value of the input.
    """
    return -operand


def squareroot(operand):
    """
    Calculates the square root of a given number.
    
    Args:
        operand (float): The number to find the square root of.
        
    Returns:
        float: The square root of the input number.
    """
    return operand**0.5


def addition(firstOperand, secondOperand):
    """
    Adds two numbers.
    
    Args:
        firstOperand (float): The first number.
        secondOperand (float): The second number.
        
    Returns:
        float: The sum of the two numbers.
    """
    return firstOperand + secondOperand


def subtraction(firstOperand, secondOperand):
    """
    Subtracts the second number from the first number.
    
    Args:
        firstOperand (float): The first number.
        secondOperand (float): The second number.
        
    Returns:
        float: The result of the subtraction.
    """
    return firstOperand - secondOperand


def multiplication(firstOperand, secondOperand):
    """
    Multiplies two numbers.
    
    Args:
        firstOperand (float): The first number.
        secondOperand (float): The second number.
        
    Returns:
        float: The product of the two numbers.
    """
    return firstOperand * secondOperand


def division(firstOperand, secondOperand):
    """
    Divides the first number by the second number.
    
    Args:
        firstOperand (float): The numerator.
        secondOperand (float): The denominator.
        
    Returns:
        float: The result of the division, or None if an error occurs.
         catches:
        ZeroDivisionError: If the second Operand is 0.
    """
    try:
        return firstOperand / secondOperand
    except ZeroDivisionError:
        print("Error: Division by zero is undefined.")
        return

def power(firstOperand, secondOperand):
    """
    Raises the first number to the power of the second number.
    
    Args:
        firstOperand (float): The base number.
        secondOperand (float): The exponent.
        
    Returns:
        float: The result of the exponentiation.
    """
    return firstOperand**secondOperand


def average(firstOperand, secondOperand):
    """
    Calculates the average of two numbers.
    
    Args:
        firstOperand (float): The first number.
        secondOperand (float): The second number.
        
    Returns:
        float: The average of the two numbers.
    """
    return (firstOperand + secondOperand) / 2


def minimal(firstOperand, secondOperand):
    """
    Returns the smaller of two numbers.
    
    Args:
        firstOperand (float): The first number.
        secondOperand (float): The second number.
        
    Returns:
        float: The smaller of the two numbers.
    """
    return firstOperand if firstOperand < secondOperand else secondOperand


def module(firstOperand, secondOperand):
    """
    Returns the remainder of the division of two numbers.
    
    Args:
        firstOperand (int): The numerator.
        secondOperand (int): The denominator.
        
    Returns:
        int: The remainder of the division.
        
    catches:
        ZeroDivisionError: If the secondOperand is 0.
    """
    try:
        return firstOperand % secondOperand
    except ZeroDivisionError:
      print("Error: module zero is undefined.")
      return NULL
