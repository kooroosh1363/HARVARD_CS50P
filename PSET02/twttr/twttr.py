vowels = ["a", "e", "i", "o", "u"]

input_txt = input("Input: ").strip()
output_txt = ""

for let in input_txt:
    if let.lower() not in vowels:
        output_txt += let

print(f"Output: {output_txt}")
