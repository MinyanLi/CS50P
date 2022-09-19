greeting = input("What do you say for greeting? ")

ci_greeting = greeting.lower().strip()

if ci_greeting[0:5] == "hello":
    print("$0")
elif ci_greeting[0] == "h":
    print("$20")
else:
    print("$100")