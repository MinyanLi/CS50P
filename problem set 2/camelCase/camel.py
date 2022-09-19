transfer = input("Camel case ")

up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

new_transfer = ""

for i in transfer:
    if up.count(i) == 0:
        new_transfer = new_transfer + i
    else:
        for j in up:
            if i == j:
                new_transfer = new_transfer + "_" + i.lower()
            else:
                continue

print(new_transfer)