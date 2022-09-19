

ask = input("Great Question of Life, the Universe and Everything ")
ci_ask = ask.lower().strip()

if ci_ask == "42" or ci_ask == "forty-two" or ci_ask == "forty two":
    print("Yes")
else:
    print("No")