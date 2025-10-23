class Stack:
    def __init__(self):
        self.items = []  # Stack implemented using a list

    def push(self, x):
        """Insert an element into the stack"""
        self.items.append(x)
        print(f"{x} pushed onto the stack.")

    def pop(self):
        """Remove and return the top element of the stack"""
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.items.pop()

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0

    def display(self):
        """Display all elements in the stack"""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):", self.items[::-1])

    def evaluate_rpn(self, expression):
        """Evaluate a Reverse Polish Notation (postfix) expression"""
        tokens = expression.split()
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                # Operand — push to stack
                self.push(int(token))
            else:
                # Operator — pop two operands
                if len(self.items) < 2:
                    print("Error: Invalid RPN expression.")
                    return None
                b = self.pop()
                a = self.pop()

                if token == '+':
                    self.push(a + b)
                elif token == '-':
                    self.push(a - b)
                elif token == '*':
                    self.push(a * b)
                elif token == '/':
                    if b == 0:
                        print("Error: Division by zero.")
                        return None
                    self.push(a / b)
                else:
                    print(f"Unknown operator: {token}")
                    return None

        if len(self.items) == 1:
            return self.pop()
        else:
            print("Error: Invalid RPN expression.")
            return None


# ---------------- MAIN MENU ----------------
def main():
    stack = Stack()

    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Evaluate RPN")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            value = input("Enter value to push: ")
            if value.lstrip('-').isdigit():
                stack.push(int(value))
            else:
                print("Invalid input! Please enter an integer.")

        elif choice == '2':
            popped = stack.pop()
            if popped is not None:
                print(f"Popped element: {popped}")

        elif choice == '3':
            stack.display()

        elif choice == '4':
            expr = input("Enter RPN Expression (e.g., 5 3 4 * +): ")
            result = stack.evaluate_rpn(expr)
            if result is not None:
                print("Result:", result)

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the main program
if __name__ == "__main__":
    main()
