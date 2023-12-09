def main():
    time_input = input("Enter the time in 24-hour format (HH:MM): ")

    # Convert the input time to hours
    try:
        hours = convert(time_input)
    except ValueError:
        print("Invalid time format. Please use HH:MM format.")
        return

    # Define meal time ranges
    breakfast_start = 7.0
    breakfast_end = 8.0
    lunch_start = 12.0
    lunch_end = 13.0
    dinner_start = 18.0
    dinner_end = 19.0

    # Check if it's mealtime and print the corresponding message
    if breakfast_start <= hours <= breakfast_end:
        print("breakfast time")
    elif lunch_start <= hours <= lunch_end:
        print("lunch time")
    elif dinner_start <= hours <= dinner_end:
        print("dinner time")


def convert(time):
    # Split the time string into hours and minutes
    parts = time.split(":")

    if len(parts) != 2:
        raise ValueError("Invalid time format. Please use HH:MM format.")

    try:
        hours = int(parts[0])
        minutes = int(parts[1])
    except ValueError:
        raise ValueError("Invalid time format. Please use HH:MM format.")

    # Check if the values are within valid ranges
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        raise ValueError("Invalid time. Hours must be between 0 and 23, and minutes between 0 and 59.")

    # Calculate the equivalent time in hours
    return hours + minutes / 60.0

if __name__ == "__main__":
    main()
