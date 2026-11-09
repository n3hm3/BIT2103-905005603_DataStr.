class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)


def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def apply_operation(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            raise ValueError("Division by zero")
        return a / b


def evaluate_expression(expression):
    values = Stack()
    operators = Stack()

    i = 0
    n = len(expression)

    while i < n:
        if expression[i] == ' ':
            i += 1
            continue

        if expression[i].isdigit():
            num = 0
            while i < n and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.push(num)
            continue

        elif expression[i] == '(':
            operators.push(expression[i])

        elif expression[i] == ')':
            while not operators.is_empty() and operators.peek() != '(':
                op = operators.pop()
                b = values.pop()
                a = values.pop()
                values.push(apply_operation(a, b, op))
            operators.pop()

        elif expression[i] in '+-*/':
            while (not operators.is_empty() and
                   operators.peek() != '(' and
                   precedence(operators.peek()) >= precedence(expression[i])):
                op = operators.pop()
                b = values.pop()
                a = values.pop()
                values.push(apply_operation(a, b, op))
            operators.push(expression[i])

        i += 1

    while not operators.is_empty():
        op = operators.pop()
        b = values.pop()
        a = values.pop()
        values.push(apply_operation(a, b, op))

    return values.pop()


def process_file(input_filename="input.txt", output_filename="output.txt"):
    with open(input_filename, "r") as infile:
        content = infile.read().strip()

    expressions = [expr.strip() for expr in content.split("----") if expr.strip()]

    results = []
    for expr in expressions:
        try:
            result = evaluate_expression(expr)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            results.append(str(result))
        except Exception as e:
            results.append(f"Error: {str(e)}")

    with open(output_filename, "w") as outfile:
        outfile.write("\n----\n".join(results))


if __name__ == "__main__":
    process_file()
    print("Evaluation complete. Results written to output.txt")