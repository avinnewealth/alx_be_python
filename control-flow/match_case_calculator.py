num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):").strip()


match operation:
    case "+":
        result = num1 + num2
        print(f"The reuslt is  {result}")
    case "-":
        result = num1 - num2
        print(f"The reuslt is  {result}")
    case "*":
        result = num1 * num2
        print(f"The reuslt is  {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation selected. Please choose +, -, *, or /.")

    
        

