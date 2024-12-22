import pytest
from BTSUniter import formatingAndValidatingInput, toReversePolish, evaluateReversePolish, CONSTANTS

def evaluate(expression):
    """
    Evaluates an expression using the calculator's workflow.
    """
    formatted = formatingAndValidatingInput(expression)
    if formatted is None:
        raise ValueError("Invalid input format.")
    rpn = toReversePolish(formatted)
    if rpn is None:
        raise ValueError("Error in RPN conversion.")
    return expression, evaluateReversePolish(rpn)

def test_basic_arithmetic():
    assert evaluate("2+2") == ("2+2", 4)
    assert evaluate("10-3") == ("10-3", 7)
    assert evaluate("4*5") == ("4*5", 20)
    assert evaluate("8/2") == ("8/2", 4.0)

def test_complex_arithmetic():
    assert evaluate("2+(3*4)") == ("2+(3*4)", 14)
    assert evaluate("(10-3)/2") == ("(10-3)/2", 3.5)
    assert evaluate("(2+3)*(5-1)") == ("(2+3)*(5-1)", 20)

def test_trigonometric_functions():
    assert abs(evaluate("S(0)")[1] - 0) < 1e-5
    assert abs(evaluate("C(0)")[1] - 1) < 1e-5
    assert abs(evaluate("T(0)")[1] - 0) < 1e-5
    assert abs(evaluate("S(p/2)")[1] - 1) < 1e-5
    assert abs(evaluate("C(p/2)")[1] - 0) < 1e-5

def test_logarithmic_functions():
    assert abs(evaluate("L(e)")[1] - 1) < 1e-5
    assert abs(evaluate("L(1)")[1] - 0) < 1e-5

def test_constants():
    assert abs(evaluate("p")[1] - CONSTANTS['p']) < 1e-5
    assert abs(evaluate("e")[1] - CONSTANTS['e']) < 1e-5

def test_previous_answer():
    assert evaluate("2+2") == ("2+2", 4)
    assert evaluate("a+3") == ("a+3", 7)

def test_unary_operations():
    assert evaluate("~5") == ("~5", -5)
    assert evaluate("!5") == ("!5", 120)
    assert evaluate("#123") == ("#123", 6)

def test_combined_operations():
    assert evaluate("S(p/2)+C0") == ("S(p/2)+C0", 2)
    assert evaluate("(2+3)*(10/L(e))") == ("(2+3)*(10/L(e))", 50)
    assert evaluate("10+~5") == ("10+~5", 5)
    assert evaluate("10+(2@4)") == ("10+(2@4)", 13)

def test_invalid_inputs():
    with pytest.raises(ValueError):
        evaluate("2++2")
    with pytest.raises(ValueError):
        evaluate("10/0")
    with pytest.raises(ValueError):
        evaluate("a+5")  # Assuming 'a' hasn't been set yet

def test_edge_cases():
    assert evaluate("0+0") == ("0+0", 0)
    assert evaluate("-0") == ("-0", 0)
    assert evaluate("0$(-1)") == ("0$(-1)", 0)
    assert evaluate("(2+3)*(-4)") == ("(2+3)*(-4)", -20)
    assert abs(evaluate("-((2$3)@(4&1))")[1] - -2) < 1e-5

def test_custom_precedence():
    assert evaluate("2^3^2") == ("2^3^2", 512)  # Right-associative exponentiation
    assert evaluate("10-(2#*2)") == ("10-(2#*2)", 6)
    assert evaluate("-2^2$4") == ("-2^2$4", -16)
    assert evaluate("(3*3)#") == ("(3*3)#", 9)

print("Enable the test commands in calculating.py if you haven't!")
