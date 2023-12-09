txt = input("Greeting: ").strip().lower()

if txt.startswith("hello"):
    jo = 0
elif txt.startswith("h"):
    jo = 20
else:
    jo = 100

print(f"${jo}")