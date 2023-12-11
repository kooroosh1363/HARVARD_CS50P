def calculate_fuel_percentage(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if y == 0 or x > y:
            return None  # Invalid input
        percentage = (x / y) * 100
        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return round(percentage)
    except (ValueError, ZeroDivisionError):
        return None  # Invalid input

while True:
    fraction_input = input("Enter a fraction (X/Y): ").strip()
    result = calculate_fuel_percentage(fraction_input)

    if result is not None:
        if result == 'E':
            print(result)
        elif result == 'F':
            print(result)
        else:
            print(f"{result}%")
        break
    else:
        print("Invalid input. Please try again.")
