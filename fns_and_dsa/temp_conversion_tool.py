
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction:

def main():
    while True:
        user_input = input("Enter a temperature (e.g., 25C or 77F) or 'exit' to quit: ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the temperature conversion tool. Goodbye!")
            break

        try:
            if user_input[-1].upper() == 'C':
                celsius = float(user_input[:-1])
                fahrenheit = convert_to_fahrenheit(celsius)
                print(f"{celsius}C is {fahrenheit}F.")
            elif user_input[-1].upper() == 'F':
                fahrenheit = float(user_input[:-1])
                celsius = convert_to_celsius(fahrenheit)
                print(f"{fahrenheit}F is {celsius}C.")
            else:
                raise ValueError("Invalid temperature format.")

        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
