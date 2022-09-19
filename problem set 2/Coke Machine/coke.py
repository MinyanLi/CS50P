total_amount = 0

while total_amount < 50:
    insert_coin = int(input("Insert Coin: "))

    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        total_amount = total_amount + insert_coin
    if total_amount >= 50:
        break
    print("Amount Due: ", 50 - total_amount)


if total_amount >= 50:
    print("Change Owed: ", total_amount - 50)




