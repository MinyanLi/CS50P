grocery_list = {}

while True:
    try:
        item = input().strip().upper()
        if item in grocery_list.keys():
            grocery_list[item] = grocery_list[item] + 1
        else:
            grocery_list.update({item: 1})

    except EOFError:
        break
print("\n")

output_list = dict(sorted(grocery_list.items()))

for i in output_list:
    print(output_list[i], i, end = "\n")



