number =int(input("Enter a number to see its multiplication table:"))
for i in range(1, 11):  # loop from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")