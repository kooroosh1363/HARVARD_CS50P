import sys
from random import choice
from pyfiglet import Figlet


f = Figlet()
fontlist = f.getFonts()


#if there were no parameters in argv to be used as font choice
if len(sys.argv) == 1:
    a = input("Input: ").strip()
    f.setFont(font=choice(fontlist))
    print(f.renderText(a))


#if the argv was complete and font could be recognzed
elif len(sys.argv) == 3:
    if str(sys.argv[1]) in ["-f", "--font"] and str(sys.argv[2]) in fontlist:
       a = input("Input: ").strip()
       f.setFont(font=str(sys.argv[2]))
       print(f.renderText(a))
    else:
        #happens when font is not found
        sys.exit("Invalid usage")

#happens when there is a problem with the whole input
else:
    sys.exit("Invalid usage")