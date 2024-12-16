MANUAL = """
Welcome to Guy's Arithmetic Calculator! Below is a detailed guide to help you use this tool effectively.

---
**General Usage:**
- Enter a calculation as a single line.
- For example: `3 + 5 * ( 2 - 4 )`
- To exit the program, type: `QUIT`
- To see this manual again, type: `HELP`

---
**Supported Features:**
1. **Basic Arithmetic:**
   - Addition (`+`)
   - Subtraction (`-`)
   - Multiplication (`*`)
   - Division (`/`)
   - Modulus (`%`)
   - Power (`^`)

2. **Advanced Operations:**
   - Maximum of two numbers (`$`)
   - Minimum of two numbers (`&`)
   - Average of two numbers (`@`)

3. **Unary Operations:**
   - Negation (`~`): Converts a number to its negative value.
   - Factorial (`!`): Computes the factorial of a number.
   - Summing Digits (`#`): Sums all the digits of a number.
   - Square Root (`Q`): Computes the square root of a number.
   - Sine (`S`): Computes an estimation of the sine of a number (in radians).
   - Cosine (`C`): Computes an estimation of the cosine of a number (in radians).
   - Tangent (`T`): Computes an estimation of the tangent of a number (in radians).
   - Natural Logarithm ('L') Computes an estimation of the natural logarithm of a number

---
**Input Rules:**
- Use parentheses `(` and `)` to define precedence as needed.
- Unary operators like `~` (negation) apply to the number or expression immediately following them.

---
**Examples:**
1. **Basic Arithmetic:**
   - Input: `3 + 5`
   - Output: `8`

2. **Mixed Operations with Precedence:**
   - Input: `3 + 5 * 2`
   - Output: `13` (multiplication has higher precedence than addition)

3. **Using Parentheses:**
   - Input: `( 3 + 5 ) * 2`
   - Output: `16` (parentheses override precedence)

4. **Unary Negation:**
   - Input: `~ 5 + 3`
   - Output: `-2` (negation applies to `5`)

5. **Factorial:**
   - Input: `5 !`
   - Output: `120`

6. **Sine of a Number:**
   - Input: `S ( 3.14159 / 2 )`
   - Output: `1.0` (sine of pi/2 radians)

7. **Combining Unary and Binary Operations:**
   - Input: `~ 4 ^ 2`
   - Output: `-16` (negation applies before exponentiation)

8. **Max and Min:**
   - Input: `5 $ 10`
   - Output: `10` (maximum of 5 and 10)
   - Input: `5 & 10`
   - Output: `5` (minimum of 5 and 10)

9. **Average of Two Numbers:**
   - Input: `4 @ 10`
   - Output: `7`

---
**Error Handling:**
- The calculator will display an error message if:
  - Input contains invalid characters or unsupported operators.
  - Parentheses are unbalanced.
  - arithmetic issues such as:
        - - Division by zero is attempted.
        - - taking a logarithm of a non positive is attempted.

Thank you for using Guy's Arithmetic Calculator! Type `HELP` anytime to see this guide again.
"""
