import Arithmatics
import stringHandling

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
SQUARE_ROOT_SYMBOL = 'Q'
SINE_SYMBOL = 'S'
COSINE_SYMBOL = 'C'
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
}

def formatingAndValidatingInput(inputString):
    """
    Transforms a string into a list of operands and numbers
    for the sake of handling calculations while maintaining
    order and ensuring valid inputs only.

    Args:
        inputString (string): A string containing the user's input
    Returns:
        The string separated into a list of operands and numbers
    Raises:
        ValueError: In case the input contains values which aren't
        a number nor a recognized operand.
    """
    transformed = stringHandling.extract_numbers_and_symbols(inputString)
    
    if any(
        item not in UNARY_OPERATIONS and 
        item not in BINARY_OPERATIONS and 
        not isinstance(item, (int, float)) 
        for item in transformed
    ):
        raise ValueError("Make sure your input is composed of exclusively valid inputs")
    
    return transformed

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

# Example Usage
if __name__ == "__main__":
    input_string = input("Enter a calculation with a space after each number and operand: ")
    formatted_input = formatingAndValidatingInput(input_string)
    rpn_expression = toReversePolish(formatted_input)
    result = evaluateReversePolish(rpn_expression)
    print(f"Result: {result}")

