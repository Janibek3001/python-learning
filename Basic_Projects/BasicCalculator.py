print("Choose 2 numbers: ")
x = int(input())
y = int(input())

print("Choose the operand (+, -, *, /)")
result = None
choice = input()

match choice:
    case '+':
        result = x + y
    case '-':
        result = x - y
    case '*':
        result = x * y
    case '/':
        if y != 0:
            result = x / y
        else:
            print("Error: Division by 0 is not acceptable")
    case _:
        print("Invalid operator!")
        
if result is not None:
    print(f"Result: {result:.2f}")