txt = input("camelCase: ").strip()

snake_case = ""
for i in txt:
    if i.isupper():
        snake_case += "_"
        snake_case += i.lower()
    else:
        snake_case += i

if snake_case.startswith("_"):
    snake_case = snake_case[1:]  

print(f"snake_case: {snake_case}")
