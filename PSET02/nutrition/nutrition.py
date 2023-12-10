fruits = [
    {"fruit": "Apple", "Calories": "130"},
    {"fruit": "Avocado", "Calories": "50"},
    {"fruit": "Banana", "Calories": "110"},
    {"fruit": "Cantaloupe", "Calories": "50"},
    {"fruit": "Grapefruit", "Calories": "60"},
    {"fruit": "Grapes", "Calories": "90"},
    {"fruit": "Honeydew ", "Calories": "50"},
    {"fruit": "Kiwifruit", "Calories": "90"},
    {"fruit": "Lemon", "Calories": "15"},
    {"fruit": "Lime", "Calories": "20"},
    {"fruit": "Orange", "Calories": "80"},
    {"fruit": "Peach", "Calories": "60"},
    {"fruit": "Pear", "Calories": "100"},
    {"fruit": "Pineapple", "Calories": "50"},
    {"fruit": "Plums", "Calories": "70"},
    {"fruit": "Strawberries", "Calories": "50"},
    {"fruit": "Sweet Cherries", "Calories": "100"},
    {"fruit": "Tangerine", "Calories": "50"},
    {"fruit": "Watermelon", "Calories": "80"}
]


txt = input("Input: ").strip().lower()
found = False

for i in fruits:
    if txt == i["fruit"].lower():
        print(f"Calories: {i['Calories']}")
        found = True
        break

if not found:
    print("")