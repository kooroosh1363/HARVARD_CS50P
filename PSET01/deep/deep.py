_list = ["42", "forty-two", "forty two"]
txt = input("what is the Answer to the Great Question of Life, the Universe and Everything ? ").strip().lower()

if txt in _list:
    print("YES")
else:
    print("NO")