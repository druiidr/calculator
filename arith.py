from math import pow


def factorial(num):    #returns the factorial value of an inputted number
    if(num==0):
        return 1
    return num*factorial()


def maximal(num1,num2):    #returns the larger of two numbers
    if(num1>num2):
        return num1
    return num2

def unaryBasicCaculation(operator,operand):    #handles unary calculation in accordance with an inputted operator and numerical value
     if operator== '~': #~=negative
            return 0-operand
     elif operator== '!': #!=factorialization
            return factorial(operand-1)

def binaryBasicCalculation(firstOperand,operator,secondOperand):     #handles binary calculation in accordance with an inputted operator and numerical values
        if operator== '+':   #+=addition
            return firstOperand+secondOperand
        elif operator== '-': #-=subtraction
            return firstOperand-secondOperand
        elif operator== '*': #*=multiplication
            return firstOperand*secondOperand
        elif operator== '/':  #/=division
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
            return firstOperand%secondOperand
        else:
            return "not a valid binary operand"

