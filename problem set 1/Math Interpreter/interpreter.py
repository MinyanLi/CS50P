cal = input("Please type an arithmetic expression: ")

x, y, z = cal.split(" ")

x = int(x)
z = int(z)

if y == "+":
    print(round(float(x + z),1))
if y == "-":
    print(round(float(x - z),1))
if y == "*":
    print(round(float(x * z),1))
if y == "/":
    print(round(float(x / z),1))




