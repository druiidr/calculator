WHITE_CHARACTERS=[' ', '\n', '\t']

def DeriveNumberFromString(strng):
    """
    Extracts a numerical value from a string of characters.
    
    Args:
        strng (string): A string containing digits.
        
    Returns:
        float: The value of the number in the string.
    """

    number = ""
    hasDecimal = False

    for char in strng:
        if char.isdigit():
            number += char
        elif char == '.' and not hasDecimal:
            number += char
            hasDecimal = True
        elif number:  # If a valid number has already started forming
            break
        else:
            raise ValueError("Number is interlaced with invalid characters (not digit or the decimal separator).")
    
    if number:
        return float(number) if '.' in number else int(number)
    else:
        raise ValueError("No numerical value found in the string.")



def extract_numbers_and_symbols(strng):
    """
    Extracts all numbers and non-digit symbols (excluding white spaces) from a string, 
    treating each character as a separate string except for numbers, which are parsed as integers or floats.
    
    Args:
        strng (string): The input string containing numbers and symbols.
        
    Returns:
        list: A list containing each character as a separate string, 
              with numbers parsed as int or float where applicable, 
              and excluding white spaces.
    """
    numbers_and_symbols = []
    temp_str = ""

    for char in strng:
        if char.isdigit() or (char == '.' and temp_str and temp_str[-1].isdigit()):
            temp_str += char
        elif temp_str:
            numbers_and_symbols.append(DeriveNumberFromString(temp_str))
            temp_str = ""
        elif char not in WHITE_CHARACTERS:
            numbers_and_symbols.append(char)

    if temp_str:
        numbers_and_symbols.append(DeriveNumberFromString(temp_str))

    return numbers_and_symbols




