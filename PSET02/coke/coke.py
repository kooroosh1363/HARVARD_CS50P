price = 50
gain = 0

while gain < price:
    print(f"Amount Due: {price - gain}")
    txt = int(input("Insert Coin: ").strip())

    if txt == 25 or txt == 10 or txt == 5:
        gain += txt
    else:
        continue

if gain > price:
    change_owed = gain - price
    print(f"Change Owed: {change_owed}")
elif gain == price:
    print("Change Owed: 0")
else:
    print("Error: Please insert more coins to complete the purchase.")
