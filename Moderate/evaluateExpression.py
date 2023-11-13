def evaluate_expression(expression):
    # Helper function to apply operators to values
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)

    # Helper function to determine operator precedence
    def precedence(operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        return 0

    # Stacks to store operators and values
    operators = []
    values = []
    i = 0

    # Loop through the expression
    while i < len(expression):
        # If the character is a digit, parse the entire number
        if expression[i].isdigit():
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            values.append(float(expression[i:j]))
            i = j
        # If the character is an operator
        elif expression[i] in "+-*/":
            # Pop operators and apply them based on precedence
            while (
                operators
                and precedence(operators[-1]) >= precedence(expression[i])
            ):
                apply_operator(operators, values)
            operators.append(expression[i])
            i += 1
        # If the character is an opening parenthesis
        elif expression[i] == "(":
            operators.append(expression[i])
            i += 1
        # If the character is a closing parenthesis
        elif expression[i] == ")":
            # Pop operators and apply them until an opening parenthesis is encountered
            while operators[-1] != "(":
                apply_operator(operators, values)
            operators.pop()  # Pop the opening parenthesis
            i += 1
        else:
            i += 1

    # Pop remaining operators and apply them
    while operators:
        apply_operator(operators, values)

    # The final result is the only value left on the values stack
    return values[0] if values else None

# Example usage:
expression = "2 + 3 * 4 - 8 / 2"
result = evaluate_expression(expression)

if result is not None:
    print(f"Result of '{expression}' is: {result}")
