import Arithmatics


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

print(UNARY_OPERATIONS['~'](12345))
print(BINARY_OPERATIONS['*'](5,4))


