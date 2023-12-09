txt_1, txt_2, txt_3 = input("enter an expression : ").strip().split(" ")

if txt_2 == "+":
    jo = float(txt_1) + float(txt_3)
elif txt_2 == "-":
    jo = float(txt_1) - float(txt_3)
elif txt_2 == "*":
    jo = float(txt_1) * float(txt_3)
elif txt_2 == "/":
    jo = float(txt_1) / float(txt_3)

print(f"{jo:.1f}")