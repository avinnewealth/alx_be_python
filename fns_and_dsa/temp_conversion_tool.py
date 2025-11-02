FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Main Program
temp_value = input("Enter the temperature to convert: ")

# Check if input is numeric
if temp_value.replace('.', '', 1).isdigit():
    temp_value = float(temp_value)
    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if temp_unit == "c":
        result = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {result:.2f}°F")

    elif temp_unit == "f":
        result = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {result:.2f}°C")

    else:
        print("Please enter a valid unit! Use 'C' for Celsius or 'F' for Fahrenheit.")

else:
    print("Invalid temperature. Please enter a numeric value.")





""" FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
100

temp_value= int(input("Enter the temperature to convert: "))
print(temp_value, type(temp_value))
if temp_value != int:
    temp_unit= input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    if temp_unit == "c":
        print(f"{temp_value}°F is {convert_to_fahrenheit(temp_value)}°C")
    elif temp_unit =="f":
        print(f"{temp_value}°F is {convert_to_celsius(temp_value)}°C")
    else:
        print("Please enter a valid unit! ")

else: print("Invalid Please enter a numeric value.")    
 """


    


