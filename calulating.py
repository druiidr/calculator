import Arithmetics
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

# Dictionary containing binary operations
BINARY_OPERATIONS = {
    ADDITION_SYMBOL: Arithmetics.addition,
    AVERAGE_SYMBOL: Arithmetics.average,
    DIVISION_SYMBOL: Arithmetics.division,
    SUBTRACTION_SYMBOL: Arithmetics.subtraction,
    MULTIPLICATION_SYMBOL: Arithmetics.multiplication,
    POWER_SYMBOL: Arithmetics.power,
    MODULU_SYMBOL: Arithmetics.module,
    MAXIMUM_SYMBOL: Arithmetics.maximal,
    MINIMUM_SYMBOL: Arithmetics.minimal
}

# Symbolizing unary operations
NEGATION_SYMBOL = '~'
FACTORIAL_SYMBOL = '!'
SUMMING_DIGIT_SYMBOL = '#'
SQUARE_ROOT_SYMBOL = 'Q'
SINE_SYMBOL = 'S'
COSINE_SYMBOL = 'C'
NATURAL_LOGARITHM_SYMBOL = 'L'
TANGENT_SYMBOL = 'T'

# Dictionary containing unary operations
UNARY_OPERATIONS = {
    NEGATION_SYMBOL: Arithmetics.negate,
    FACTORIAL_SYMBOL: Arithmetics.factorial,
    SQUARE_ROOT_SYMBOL: Arithmetics.squareroot,
    SINE_SYMBOL: Arithmetics.taylorSine,
    COSINE_SYMBOL: Arithmetics.taylorCosine,
    TANGENT_SYMBOL: Arithmetics.tangent,
    SUMMING_DIGIT_SYMBOL: Arithmetics.digitSum,
    NATURAL_LOGARITHM_SYMBOL: Arithmetics.taylorLn,
}
# Symbolizing mathematical constants
EULER_SYMBOL = 'e'
PI_SYMBOL = 'p'

#dictionary containing mathematical constants
CONSTANTS ={
    EULER_SYMBOL:Arithmetics.EULERS_CONSTANT,
    PI_SYMBOL:Arithmetics.PI}

def formatingAndValidatingInput(inputString):
    """
    Parses and validates input, handling negative numbers and unary operators generically.

    Args:
        inputString (str): The user's input expression.
    Returns:
        list: A list of tokens (numbers and operators).
    """
    try:
        tokens = stringHandling.extract_numbers_and_symbols(inputString)  # Tokenize input
        result = []
        
        for i, token in enumerate(tokens):
            # Handle unary negation for numbers (e.g., `-4`)
            if token == '-' and (i == 0 or tokens[i - 1] in BINARY_OPERATIONS or tokens[i - 1] == '('):
                result.append('~')  # Replace '-' with unary negation symbol
            elif token in CONSTANTS:
                result.append(CONSTANTS[token])  # Replace mathematical constant with its value
            else:
                result.append(token)

        # Validate tokens
        for i, item in enumerate(result):
            if item not in UNARY_OPERATIONS and item not in BINARY_OPERATIONS \
                    and item != '(' and item != ')' and not isinstance(item, (int, float)):
                raise ValueError(f"Invalid token: {item}")

            # Check for consecutive operands without an operator
            if ((i > 0 and isinstance(result[i - 1], (int, float)) and isinstance(item, (int, float))) or
                (i > 0 and result[i - 1] in CONSTANTS.values() and item in CONSTANTS.values()) or
                 (i > 0 and isinstance(result[i - 1], (int, float)) and item == '(')):
             raise ValueError(f"Consecutive operands found: {result[i - 1]} and {item}") 
        
        return result
    except Exception as e:
        print(f"Error during input validation: {e}")
        return None


def toReversePolish(tokens):
    """
    Converts a list of tokens into Reverse Polish Notation (RPN)
    using the Shunting Yard Algorithm to maintain the correct order of operations.

    Args:
        tokens (list): A list of tokens (operands and operators)
    Returns:
        list: A list of tokens in RPN order
    """
    precedence = {
        ADDITION_SYMBOL: 1, SUBTRACTION_SYMBOL: 1,
        MULTIPLICATION_SYMBOL: 2, DIVISION_SYMBOL: 2, MODULU_SYMBOL: 2,
        POWER_SYMBOL: 3
    }
    right_associative = {POWER_SYMBOL}
    output = []
    operators = []
    try:
        for i, token in enumerate(tokens):
            # Append numbers directly to the output queue
            if isinstance(token, (int, float)):
                output.append(token)
                # Handle immediate evaluation of unary operators after numbers
                while operators and operators[-1] in UNARY_OPERATIONS and operators[-1] != FACTORIAL_SYMBOL:
                    output.append(operators.pop())
            # Unary operators are pushed onto the stack
            elif token in UNARY_OPERATIONS:
                if token == FACTORIAL_SYMBOL:
                    output.append(token)  # Factorial works on the previous operand
                else:
                    operators.append(token)
            # Binary operators require precedence checks
            elif token in BINARY_OPERATIONS:
                while (operators and operators[-1] in precedence and
                       (precedence[operators[-1]] > precedence[token] or
                        (precedence[operators[-1]] == precedence[token] and token not in right_associative))):
                    output.append(operators.pop())
                operators.append(token)
            # Handle parentheses
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Remove the '(' from stack
        # Pop remaining operators
        while operators:
            output.append(operators.pop())
        return output
    except Exception as e:
        print(f"Error during RPN conversion: {e}")
        return None

def evaluateReversePolish(rpn_tokens):
    """
    Evaluates a list of tokens in Reverse Polish Notation (RPN).

    Args:
        rpn_tokens (list): A list of tokens in RPN order
    Returns:
        float: The evaluation result
    """
    stack = []
    try:
        for token in rpn_tokens:
            # Numbers are pushed onto the stack
            if isinstance(token, (int, float)):
                stack.append(token)
            # Binary operations pop two operands and apply the operation
            elif token in BINARY_OPERATIONS:
                b = stack.pop()
                a = stack.pop()
                stack.append(BINARY_OPERATIONS[token](a, b))
            # Unary operations pop one operand and apply the operation
            elif token in UNARY_OPERATIONS:
                a = stack.pop()
                stack.append(UNARY_OPERATIONS[token](a))
        return stack.pop()
    except IndexError:
        print("Error: Missing operands or mismatched operators.")
        return None
    except Exception as e:
        print(f"Error during evaluation: {e}")
        return None

if __name__ == "__main__":
    input_string = ""
    while input_string != "QUIT":
        input_string = input("Enter a calculation, type HELP for the manual, or QUIT to exit: \n\n")
        if input_string == "HELP":
            print(Manual.MANUAL)
        elif input_string == "QUIT":
            break
        else:
            formatted_input = formatingAndValidatingInput(input_string)
            if formatted_input is not None:
                rpn_expression = toReversePolish(formatted_input)
                if rpn_expression is not None:
                    result = evaluateReversePolish(rpn_expression)
                    # debug
                    # print(formatted_input)
                    # print(rpn_expression)
                    print(f"\n\nResult: {result}\n\n")
    print("Thank you!")
