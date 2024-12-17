WHITE_CHARACTERS = [' ', '\n', '\t']


def DeriveNumberFromString(strng):
    """
    Extracts a numerical value from a string of characters.
    
    Args:
        strng (string): A string containing digits.
        
    Returns:
        float or int: The value of the number in the string.
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
        list: A list containing numbers as int/float and symbols as individual strings.
    """
    numbers_and_symbols = []
    temp_str = ""
    for char in strng:
        if char.isdigit() or (char == '.' and temp_str and temp_str[-1].isdigit() and '.' not in temp_str):
            temp_str += char  # Build the number
        else:
            if temp_str:  # If a number string was being formed, append it
                numbers_and_symbols.append(DeriveNumberFromString(temp_str))
                temp_str = ""
            if char not in WHITE_CHARACTERS:  # Add symbols, skipping white characters
                numbers_and_symbols.append(char)

    if temp_str:  # Append the last number, if any
        numbers_and_symbols.append(DeriveNumberFromString(temp_str))

    return numbers_and_symbols

if __name__ == "__main__":
    print("you can't do calculations in this page! please go to calculating.py")
