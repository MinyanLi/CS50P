say = input("What do you want to say? ")

vowels = "AEIOUaeiou"

new_say = ""

for i in say:
    if vowels.count(i) == 0:
        new_say = new_say + i

print(new_say)
