# Function to convert a prefix expression to a postfix expression
def prefix_to_postfix(expression):
    stack = []  # Stack to store operands
    operators = ['+', '-']  # List of operators
    expression = expression.split()  # Split the expression into tokens

    # Iterate over the tokens in reverse order
    for token in reversed(expression):
        if token in operators:
            # Pop two operands from the stack for an operator
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Push the combined postfix expression back to the stack
            stack.append(operand1 + ' ' + operand2 + ' ' + token)
        else:
            # Push operand onto the stack
            stack.append(token)

    # Return the postfix expression
    return stack[0]

# Read the first line of input
line = input()
# Process each line until the input is "0"
while line != "0":
    # Convert the prefix expression to postfix and print it
    print(prefix_to_postfix(line))
    # Read the next line of input
    line = input()
