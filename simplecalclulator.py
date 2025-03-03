
#the code below is for a simple calculator that can perform addition, subtraction, multiplication and division
#include exception handling for division by zero

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            
        elif choice == '4':
            try:
                print(num1, "/", num2, "=", divide(num1, num2))
            except ZeroDivisionError:
                print("Cannot divide by zero")
        break