def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def main():
    print("Simple Calculator (type 'q' to quit)")
    while True:
        op = input("Operation (+, -, *, /): ").strip()
        if op.lower() == "q":
            print("Goodbye!")
            break
        if op not in OPERATIONS:
            print("Unknown operation, try again.")
            continue
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue
        print("Result:", OPERATIONS[op](a, b))


if __name__ == "__main__":
    main()