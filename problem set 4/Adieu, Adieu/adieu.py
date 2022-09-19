import inflect
p = inflect.engine()

nl = []

while True:
    try:
        n = input("Name: ").strip().capitalize()
        nl = nl + [n]
    except EOFError:
        break
print("\n")

j = p.join(nl)

print("Adieu, adieu, to", j)