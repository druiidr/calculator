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
        none
    """
    input_string = ""
    while input_string.lower() != QUIT_MESSEGE.lower():
        input_string = input("Enter a calculation, type HELP for the manual, or QUIT to exit: \n\n")
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
                    # debug commands. unable them if you want, but they are by any means not required for proper execution
                    #print(formatted_input)
                    #print(rpn_expression)
                    #debug commands end
                    print(f"\n\nResult: {result}\n\n")
    print("Thank you!")
if __name__ == "__main__":
    run_calculator()

