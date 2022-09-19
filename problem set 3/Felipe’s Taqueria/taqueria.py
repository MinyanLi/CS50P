item ={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

Total = 0

while True:
    try:
        order = input("What do you want to order? ").strip().title()
        price = item[order]
        Total = round((Total + price),3)
        print("$",end = "")
        print(f"{Total:.2f}")
    except EOFError:
        break
    except KeyError:
        pass
print("\n")
