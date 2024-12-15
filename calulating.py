import Arithmatics
import stringHandling
import Manual
# Symbolizing binary operations
ADDITION_SYMBOL = '+'
SUBTRACTION_SYMBOL = '-'
MULTIPLICATION_SYMBOL = '*'
DIVISION_SYMBOL = '/'
POWER_SYMBOL = '^'
MODULU_SYMBOL = '%'
MAXIMUM_SYMBOL = '$'
MINIMUM_SYMBOL = '&'
AVERAGE_SYMBOL = '@'

"""
Dictionary containing all binary operation functions
from support class Arithmatics.py and their associated signings
in accordance with the exercise.
"""
BINARY_OPERATIONS = {   
   ADDITION_SYMBOL: Arithmatics.addition,
   AVERAGE_SYMBOL: Arithmatics.average,
   DIVISION_SYMBOL: Arithmatics.division,
   SUBTRACTION_SYMBOL: Arithmatics.subtraction,
   MULTIPLICATION_SYMBOL: Arithmatics.multiplication,
   POWER_SYMBOL: Arithmatics.power,
   MODULU_SYMBOL: Arithmatics.module,
   MAXIMUM_SYMBOL: Arithmatics.maximal,
   MINIMUM_SYMBOL: Arithmatics.minimal
}

# Symbolizing unary operations
NEGATION_SYMBOL = '~'
FACTORIAL_SYMBOL = '!'
SUMMING_DIGIT_SYMBOL='#'
SQUARE_ROOT_SYMBOL = 'Q'
SINE_SYMBOL = 'S'
COSINE_SYMBOL = 'C'
NATURAL_LOGARITHM_SYMBOL = 'L'
TANGENT_SYMBOL = 'T'

"""
Dictionary containing all unary operation functions
from support class Arithmatics.py and their associated signings
in accordance with the exercise.
"""
UNARY_OPERATIONS = {   
   NEGATION_SYMBOL: Arithmatics.negate,
   FACTORIAL_SYMBOL: Arithmatics.factorial,
   SQUARE_ROOT_SYMBOL: Arithmatics.squareroot,
   SINE_SYMBOL: Arithmatics.taylorSine,
   COSINE_SYMBOL: Arithmatics.taylorCosine,
   TANGENT_SYMBOL: Arithmatics.tangent,
   SUMMING_DIGIT_SYMBOL:Arithmatics.digitSum,
   NATURAL_LOGARITHM_SYMBOL:Arithmatics.taylorLn,
}

def formatingAndValidatingInput(inputString):
    """
    Parses and validates input, handling negative numbers and unary operators generically.

    Args:
        inputString (str): The user's input expression.
    Returns:
        list: A list of tokens (numbers and operators).
    Raises:
        ValueError: If input contains invalid tokens.
    """
    tokens = stringHandling.extract_numbers_and_symbols(inputString)  # Tokenize input
    result = []
    for i, token in enumerate(tokens):
        # Handle unary negation for numbers (e.g., `-4`)
        if token == '-' and (i == 0 or tokens[i - 1] in BINARY_OPERATIONS or tokens[i - 1] == '('):
            result.append('~')  # Replace '-' with unary negation symbol
        else:
            result.append(token)

    # Validate tokens
    if any(
        item not in UNARY_OPERATIONS and 
        item not in BINARY_OPERATIONS and 
        item != '(' and item != ')' and
        not isinstance(item, (int, float))
        for item in result
    ):
        raise ValueError("Invalid input: Only numbers, operators, and parentheses are allowed.")

    return result

def toReversePolish(tokens):
    """
    Converts a list of tokens into Reverse Polish Notation (RPN)
    using the Shunting Yard Algorithm to maintain the correct order of operations.

    Args:
        tokens (list): A list of tokens (operands and operators)
    Returns:
        A list of tokens in RPN order
    """
    precedence = {
        ADDITION_SYMBOL: 1, SUBTRACTION_SYMBOL: 1,
        MULTIPLICATION_SYMBOL: 2, DIVISION_SYMBOL: 2, MODULU_SYMBOL: 2,
        POWER_SYMBOL: 3
    }
    right_associative = {POWER_SYMBOL}
    output = []
    operators = []

    for token in tokens:
        if isinstance(token, (int, float)):  # Numbers
            output.append(token)
        elif token in BINARY_OPERATIONS:  # Binary operators
            while (operators and operators[-1] in precedence and
                   (precedence[operators[-1]] > precedence[token] or
                    (precedence[operators[-1]] == precedence[token] and token not in right_associative))):
                output.append(operators.pop())
            operators.append(token)
        elif token in UNARY_OPERATIONS:  # Unary operators
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Remove the '(' from stack
    while operators:
        output.append(operators.pop())
    return output

def evaluateReversePolish(rpn_tokens):
    """
    Evaluates a list of tokens in Reverse Polish Notation (RPN).

    Args:
        rpn_tokens (list): A list of tokens in RPN order
    Returns:
        The evaluation result
    """
    stack = []
    for token in rpn_tokens:
        if isinstance(token, (int, float)):  # Numbers
            stack.append(token)
        elif token in BINARY_OPERATIONS:  # Binary operators
            b = stack.pop()
            a = stack.pop()
            stack.append(BINARY_OPERATIONS[token](a, b))
        elif token in UNARY_OPERATIONS:  # Unary operators
            a = stack.pop()
            stack.append(UNARY_OPERATIONS[token](a))
    return stack.pop()


if __name__ == "__main__":
    input_string =""
    while(input_string!="QUIT"):
        input_string = input("Enter a calculation with a space after each number and operand,type HELP for the manual, or QUIT to exit: \n\n")
        if input_string == "HELP":
            print(Manual.MANUAL)
        else:
            formatted_input = formatingAndValidatingInput(input_string)
            rpn_expression = toReversePolish(formatted_input)
            result = evaluateReversePolish(rpn_expression)
            print(f"\n\nResult: {result}\n\n")
    print(f"thank you!!!")

