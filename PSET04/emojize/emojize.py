import emoji as e

a = str(input("Input: ").strip())
print(f"Output: {e.emojize(a, language='alias')}")