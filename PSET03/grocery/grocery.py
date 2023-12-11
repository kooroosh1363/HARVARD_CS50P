

list = []

while True:

    try:
        a = input().strip().lower()
        list.append(a)

    except (EOFError, KeyError):
        b = sorted(set(list))
        print("\n".join(f"{list.count(i)} {i.upper()}" for i in b))
        quit()
