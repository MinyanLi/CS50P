from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

l = len(sys.argv)
fonts = figlet.getFonts()
lf = len(fonts)
f = 0


if l!= 1 and l != 3:
    sys.exit("Invalid usage")

if l == 1:
    ranfont = random.choice(fonts)
    figlet.setFont(font = ranfont)

if l == 3:
    a = sys.argv[1]
    b = sys.argv[2]
    for i in range(lf):
        if b == fonts[i]:
            f = f + 1
    if f == 0 or (a != "-f" and a != "--font"):
        sys.exit("Invalid usage")
    figlet.setFont(font=b)



text = input()
print(figlet.renderText(text))