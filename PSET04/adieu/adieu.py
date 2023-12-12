import inflect


#hell! this is sooooo cool!
p = inflect.engine()
names = []


while True:

    #getting user input
    try:
        a = str(input("Name: ")).strip()
        names.append(a)
    #wait for ctrl+d to stop the code
    except (EOFError, KeyError):
        print(f"Adieu, adieu, to {p.join(names)}", end="\n")
        quit()
