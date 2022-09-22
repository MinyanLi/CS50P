
import sys
from tabulate import tabulate
import csv
from collections import Counter
import random

def main():
    filename = "fruit_price.csv"
    pl = print_list(filename)
    print('Please enter item you want to buy. After entering each item, click "Entr". When finish all the items, click "Control + D" to end the input.')
    total = 0
    cart = []
    while True:
        try:
            order = input("Item: ").strip().lower()
            c = collect_item(pl, order)
            cart.append(order)
            total = total + c
            print("cart: ", sep="", end=" ")
            print(MyCounter(Counter(cart)))
            print("total: $" + f"{total:.2f}\n")
        except EOFError:
            final = discount(total)
            if total == final:
                print(f"Total cost is ${total:.2f}.\n")
            else:
                print(f"Total cost before discount is ${total:.2f}.")
                print(f"Total cost after discount is ${final:.2f}.")
                print(f"You saved ${(total-final):.2f}.\n")
            break
        except KeyError:
            pass



def print_list(filename):
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            fruits = []
            fruits2 = []
            for row in reader:
                fruits.append({"fruit_name": row["fruit_name"], "price": row["price"]})
                fruits2.append({row["fruit_name"]: row["price"]})
            fruits3 = {}
            for i in range(len(fruits2)):
                fruits3.update(fruits2[i])
            try:
                if len(sys.argv) == 2:
                    if sys.argv[1] == "fruit_name":
                        fruits_name_asc = []
                        for i in sorted(fruits, key = lambda sample: sample["fruit_name"]):
                            fruits_name_asc.append({"fruit_name":i["fruit_name"], "price":i["price"]})
                        print(tabulate(fruits_name_asc, headers = "keys" , tablefmt="grid"))
                    elif sys.argv[1] == "price":
                        fruits_price_asc = []
                        for i in sorted(fruits, key = lambda sample: sample["price"]):
                            fruits_price_asc.append({"fruit_name":i["fruit_name"], "price":i["price"]})
                        print(tabulate(fruits_price_asc, headers = "keys" , tablefmt="grid"))
                else:
                    print(tabulate(fruits, headers = "keys" , tablefmt="grid"))
            except IndexError:
                print(tabulate(fruits, headers = "keys" , tablefmt="grid"))
            return fruits3
    except FileNotFoundError:
        sys.exit("file does not exist")



def collect_item(fruits, order):
    price_with_tag = fruits[order]
    price = price_with_tag.split("$")[1]
    price = float(price)
    return price


class MyCounter(Counter):
    def __str__(self):
        return "".join('{} {}, '.format(k, v) for k, v in self.items())


def discount(n):
    if 0 <= n < 50:
        m = n
        print("\n\nno discount")
    elif n >= 50:
        i = random.randint(0, 50) * 0.01
        m = n * (1 - i)
        print(f"\n\nCongratulations!!! You get {round(i *100)}% off!!!")
    return m





if __name__ == "__main__":
    main()

