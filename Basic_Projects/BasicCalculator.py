print("Enter the two numbers: ")
x = float(input())
y = float(input())

print("Choose what operand do you wanna do (*, /, +, -): ")
choice = input()
result = 0;

match choice:
    case '*':
        result = x * y;
    case '-':
        result = x - y;
    case '+':   
        result = x + y
    case '/':
        result = x / y
        
print(result) 