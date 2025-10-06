def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats (may raise ValueError)
        num = float(numerator)
        den = float(denominator)

        # Perform division (may raise ZeroDivisionError)
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
