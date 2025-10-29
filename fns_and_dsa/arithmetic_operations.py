def perform_operation(num1, num2, operation):


    match operation.lower().strip() :
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Cannot divide by zero"
            elif num2 > 0:
               return num1 / num2
            else:
                return "Sorry! You can only Add, Subtract, Multiply, and Divide. Try again"
