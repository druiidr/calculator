import Arithmatics
import stringHandling


#symbolising binary operations
ADDITION_SYMBOL='+'
SUBTRACTION_SYMBOL='-'
MULTIPLICATION_SYMBOL='*'
DIVISION_SYMBOL='/'
POWER_SYMBOL='^'
MODULU_SYMBOL='%'
MAXIMUM_SYMBOL='$'
MINIMUM_SYMBOL='&'
AVERAGE_SYMBOL='@'
"""
   dictionary containing all binary operation functions
from support class Arithmatics.py and their assosiated signings
in accorence with the excercise
 """
BINARY_OPERATIONS ={   
   
   ADDITION_SYMBOL:Arithmatics.addition,
   AVERAGE_SYMBOL:Arithmatics.average,
  DIVISION_SYMBOL:Arithmatics.division,
  SUBTRACTION_SYMBOL:Arithmatics.subtraction,
  MULTIPLICATION_SYMBOL:Arithmatics.multiplication,
   POWER_SYMBOL:Arithmatics.power,
  MODULU_SYMBOL:Arithmatics.module,
  MAXIMUM_SYMBOL:Arithmatics.maximal,
  MINIMUM_SYMBOL:Arithmatics.minimal
 }
# symbolising unary operations
NEGATION_SYMBOL='~'
FACTORIAL_SYMBOL='!'
SQUARE_ROOT_SYMBOL='Q'
SINE_SYMBOL='S'
COSINE_SYMBOL='C'
TANGENT_SYMBOL='T'


"""
   dictionary containing all unary operation functions
from support class Arithmatics.py and their assosiated signings
in accorence with the excercise
 """
UNARY_OPERATIONS ={   
   
   NEGATION_SYMBOL:Arithmatics.negate,
   FACTORIAL_SYMBOL:Arithmatics.factorial,
  SQUARE_ROOT_SYMBOL:Arithmatics.squareroot,
  SINE_SYMBOL:Arithmatics.taylorSine,
  COSINE_SYMBOL:Arithmatics.taylorCosine,
   TANGENT_SYMBOL:Arithmatics.tangent,
 }

def formatingAndValidatingInput(inputString):
    """
    transforms a string into a list of operands and number 
    for the sake of handling calculations
   while maintaining order and ensuring valid inputs only.

    Args:
        inputString(string):a string containing the user's input
    Returns:
        the string seperated into a list of operands and numbers
    Raises:
        value error:in case the input contained values which arent a number nor a recognized operand
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

print(UNARY_OPERATIONS['Q'](stringHandling.DeriveNumberFromString("144")))
print(BINARY_OPERATIONS['@'](5,4))
input_string = str(input("Enter a calculation with a space after each number and operand: "))  # Fixed the syntax here
formatted_input = formatingAndValidatingInput(input_string)
print(formatted_input)


