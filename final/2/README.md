# Fruit Shop Discount Calculator
#### Video Demo:  https://youtu.be/B4MBPYQ12Kk
#### Description:
**Scenario:**
A fruit shop is having a promotion. If total price over $50, the customer is entitled to paticipate in a lottery to get 0-50% discount for the bill.
By using this calculator, users can check the price list with different sorting strategies. The calculator also collects and add up the items the customers buy. Total cost is calculated and a lottery of discount is applied. Final cost and saved cost after discount will also be shown to the customer.

##### Function explaination
**main()**
The csv file of the fruit price is imported and transformed to dictionaries for further calculations.
There a loop of Item input asking the customers to input the items they want to buy. One item at a time. After all the item input, type "Control + D" to stop the prompt. If the input is not on the fruit list, the function will prompt again. If the item is on the list, price is get from the collect_item() function. Item/order add up to the list cart. Price add up to variable total. Cart and total will be print out after every round of input for user to see. Discount, total cost before and after discount, saved money will also be calculated and print out.
'''
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
'''

**print_list()**
This is to print out the price list so that the customer can choose what they want. Customors can also chose to have the list sorted by fruit name or by price. If customer do not add command line argument, the list will not be sorted. If customer use command line argument "fruit_name", the list will be sorted by fruit name in ascending order. If customer use command line argument "price", the list will be sorted by price in ascending order. Unexpected command line argument will print the unsorted list.

This function opens the price list csv file and read it into 2 differnt structure of dictionaries. The fruits dictionary is suitable for using tabulate to output a table. The fruits2 dictionary is suitable for combining to a fruits3 dictionary and for further value extraction.
'''
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
'''

This function also use command line arguments to sort how the table looks like. If command line argument is "fruit_name", then the list will be sorted according to the fruit name in ascending order. If command line argument is "price", then the list will be sorted according to the price in ascending order.
'''
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
'''

**collect_item()**
This function converts user input of what they want to buy into the price of the product.
The fuirts argument is the dictionary of fruit name and price. The order argument is the item that the user wants to buy.
'''
def collect_item(fruits, order):
    price_with_tag = fruits[order]
    price = price_with_tag.split("$")[1]
    price = float(price)
    return price
'''

**discount()**
This function is to generate discount between 0-50% off and calculate the final cost.
If the total cost is less than $50, there's no discount.
If the total cost is more than or equal to $50, a random number is gerated and give a random discount between 0-50% off.
The final cost m is calculated and returned.
'''
def discount(n):
    if 0 <= n < 50:
        m = n
        print("\n\nno discount")
    elif n >= 50:
        i = random.randint(0, 50) * 0.01
        m = n * (1 - i)
        print(f"\n\nCongratulations!!! You get {round(i *100)}% off!!!")
    return m
'''

