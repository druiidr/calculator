def factorial(num):    #returns the factorial value of an inputted number
   if num < 0:
        raise ValueError("attempted to factorialize a non integer")
   if(num==0):
        return 1
   return num*factorial(num-1)

def taylorSine(num):  #aproximates sin(x) using the taylor series
      sum = 0
      for i in range(10):
        term = ((-1)**i * num**(2*i + 1)) / factorial(2*i + 1)
        sum += term
      return sum



def taylorCosine(num):  #aproximates cos(x) using the taylor series
      sum = 0
      for i in range(10):
        term = ((-1)**i * num**(2*i )) / factorial(2*i )
        sum += term
      return sum

def tangent(num): #aproximates tan(x) using its trigonometric definition
    return taylorSine(num)/taylorCosine(num)
def maximal(num1,num2):    #returns the larger of two numbers
    if(num1>num2):
        return num1
    return num2

def unaryBasicCaculation(operator,operand):    #handles unary calculation in accordance with an inputted operator and numerical value
     if(type(operand)!=int and type(operand)!=float) :
          raise ValueError("input involves none numbers. cant operate on those!")
     if operator== '~': #~=negative
            return 0-operand
     elif operator== '!': #!=factorialization
            return factorial(operand-1)
     elif operator=='Q':  #Q=square root
         return operand**0.5
     elif operator=='S': #S=sine
         return taylorSine(operand)
     elif operator=='C': #C=cosine
         return taylorCosine(operand)
     elif operator=='T': #T=tangent
         return tangent(operand)
     return "not a valid binary operand"


def binaryBasicCalculation(firstOperand,operator,secondOperand):     #handles binary calculation in accordance with an inputted operator and numerical values
        if operator== '+':   #+=addition
            return firstOperand+secondOperand
        elif operator== '-': #-=subtraction
            return firstOperand-secondOperand
        elif operator== '*': #*=multiplication
            return firstOperand*secondOperand
        elif operator== '/':  #/=division
            if secondOperand == 0:
                raise ZeroDivisionError("attempted division by 0")
            return firstOperand/secondOperand
        elif operator== '^':  #^=power
            return firstOperand**secondOperand
        elif operator== '@': #@=average
            return (firstOperand+secondOperand)/2
        elif operator== '$': #$=maximal value
            return maximal(firstOperand,secondOperand)
        elif operator== '&': #&=minimal value
            return 0-maximal(0-firstOperand,0-secondOperand)
        elif operator== '%': #%=module
             if secondOperand == 0:
                raise ZeroDivisionError("attempted division by 0")
             return firstOperand%secondOperand
        return "not a valid binary operand"

