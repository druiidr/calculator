import BTSUniter
import Manual

HELP_MESSEGE="HELP"
QUIT_MESSEGE="QUIT"
def run_calculator():
    """
    Creates The actual calculator and runs its ui(help,quit,user inputs,error display ect)
   and calculations(recieving an input string and printing its result)
    Args:
        none
    Returns:
        none(unless in debug mode, when it returns the answer)
    cathces:
        EOF exceptions, KeyboardInterupt
    """
    input_string = ""
    while input_string.lower() != QUIT_MESSEGE.lower():
        try:
            input_string = input("Enter a calculation, type HELP for the manual, or QUIT to exit: \n\n")
        except KeyboardInterrupt:
            print("ctrl c is not an arithmetic statement!")
        except EOFError:
            print("out of bounds buddy")
        if input_string.lower() == HELP_MESSEGE.lower():
            print(Manual.MANUAL)
        elif input_string.lower() == QUIT_MESSEGE.lower():
            break
        else:
            formatted_input = BTSUniter.formatingAndValidatingInput(input_string)
            if formatted_input is not None:
                rpn_expression = BTSUniter.toReversePolish(formatted_input)
                if rpn_expression is not None:  
                    result = BTSUniter.evaluateReversePolish(rpn_expression)
                    BTSUniter.CONSTANTS[BTSUniter.PREVIOUS_ANSWER_SYMBOL]=result
                    # debug and test commands. enable them if you want, but they are by any means not required for proper execution outside the parameters of tests and debug
                    #print(formatted_input)
                    #print(rpn_expression)
                    #return result
                    #debug commands end
                    print(f"\n\nResult: {result}\n\n")
    print("Thank you!")


if __name__ == "__main__":
    run_calculator()

