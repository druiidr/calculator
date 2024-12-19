TAYLOR_SERIES_REPETITIONS=10
EULERS_CONSTANT=2.7182818284590452353602874713527 
PI=3.141592653589793238462643383279502884197169
LN_2 = 0.69314718056
TRIGONOMETRIC_ACCURACY_EDGE=2*PI
ESTIMATIONS_MAX_EXPECTED_ACCURACY_FACTOR=100000000


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
    if num < 0 or num%1!=0:
        raise ValueError("Attempted to factorialize a non-integer.")
    if num == 0:
        return 1
    return float(num) * factorial(num - 1)

def digitSum(num):
    """
    Returns the sum of the digits of a given number.
    
    Args:
        num (float): The number to sum.
        
    Returns:
      int: sum of the digits of the input number..
     """
    num_str = str(num).replace('.', '')
    if('e' in num_str):
        raise ValueError("can only sum digits for decimal numbers outside the bounds of float")
    num = sum(int(digit) for digit in num_str)
    
    return num

def taylorLn(x):
    """
    Approximates ln(x) using a Taylor series expansion with manual range reduction.

    Args:
        x (float): The number to compute the natural logarithm for (x > 0).

    Returns:
        float: The approximate value of ln(x).

    Raises:
        ValueError: If x <= 0 since ln(x) is undefined for non-positive values.
    """
    if x <= 0:
        raise ValueError("ln(x) is undefined for x <= 0")

    # Range reduction
    multConstant = 0
    while x >= 2: 
        x /= 2
        multConstant += 1
    while x < 1:
        x *= 2
        multConstant -= 1
    # Compute ln(x) for x in [1, 2) using the Taylor series
    numerator = (x - 1)
    denominator = (x + 1)
    fraction = numerator / denominator

    total = 0
    for n in range(TAYLOR_SERIES_REPETITIONS):
        term = (1 / (2 * n + 1)) * (fraction ** (2 * n + 1))
        total += 2*term

    # Combine results using 
    formatted=int(ESTIMATIONS_MAX_EXPECTED_ACCURACY_FACTOR*(multConstant * LN_2 + total))
    return formatted/ESTIMATIONS_MAX_EXPECTED_ACCURACY_FACTOR

def rangeReductionForTrig(num):
    """
    reduces the value of num while maintaining sin(num) and cos(num)
    to ensure proper estimation. based on sin(a)=sin(180-a)
    
    Args:
        num (float): The angle in radians.
        
    Returns:
        the comparable value to num within the computable range
    """
    num = num % (2 * PI)
    return num - (2 * PI) if num > PI else num




def taylorSine(num):
    """
    Approximates sin(x) using the Taylor series expansion.
    
    Args:
        num (float): The angle in radians.
        
    Returns:
        float: The approximate value of sin(x).
    """
    num=rangeReductionForTrig(num)
    total = 0
    for i in range(TAYLOR_SERIES_REPETITIONS):
        term = ((-1)**i * num**(2 * i + 1)) / factorial(2 * i + 1)
        total += term
    total=int(total*ESTIMATIONS_MAX_EXPECTED_ACCURACY_FACTOR)
    return total/ESTIMATIONS_MAX_EXPECTED_ACCURACY_FACTOR


def taylorCosine(num):
    """
    Approximates cos(x) using the Taylor series expansion.
    
    Args:
        num (float): The angle in radians.
        
    Returns:
        float: The approximate value of cos(x).
    """
    num=rangeReductionForTrig(num)
    total = 0
    for i in range(TAYLOR_SERIES_REPETITIONS):
        term = ((-1)**i * num**(2 * i)) / factorial(2 * i)
        total += term
    total=int(total*ESTIMATIONS_MAX_EXPECTED_ACCURACY_FACTOR)
    return total/ESTIMATIONS_MAX_EXPECTED_ACCURACY_FACTOR


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
      return None


if __name__ == "__main__":
    print("you can't do calculations in this page! please go to calculating.py")
