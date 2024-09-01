def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def get_user_input():
    temp_value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
    return temp_value, unit

def convert_temperature(value, unit):
    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return fahrenheit, kelvin
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return celsius, kelvin
    elif unit == 'K':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return celsius, fahrenheit
    else:
        print("Invalid unit entered.")
        return None

def display_results(original_value, original_unit, converted_values):
    if original_unit == 'C':
        print(f"{original_value}°C is equal to {converted_values[0]:.2f}°F and {converted_values[1]:.2f}K")
    elif original_unit == 'F':
        print(f"{original_value}°F is equal to {converted_values[0]:.2f}°C and {converted_values[1]:.2f}K")
    elif original_unit == 'K':
        print(f"{original_value}K is equal to {converted_values[0]:.2f}°C and {converted_values[1]:.2f}°F")

def main():
    temp_value, unit = get_user_input()
    converted_values = convert_temperature(temp_value, unit)
    if converted_values:
        display_results(temp_value, unit, converted_values)

if __name__ == "__main__":
    main()
    input()
