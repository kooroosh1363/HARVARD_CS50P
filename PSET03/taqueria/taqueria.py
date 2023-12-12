menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total_cost = 0.00

while True:
    try:
        item = input("Enter an item: ").strip().lower()
        if item in menu:
            total_cost += menu[item]
            print(f"Total: ${total_cost:.2f}")
        else:
            print("Invalid item. Please try again.")
    except EOFError:
        break
