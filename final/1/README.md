# Fruit Shop Discount Calculator
#### Video Demo:  https://youtu.be/B4MBPYQ12Kk
#### Description:
##### Scenario:
A fruit shop is having a promotion.
If total price over $50, the customer is entitled to paticipate in a lottery to get 0-50% discount for the bill.
---
##### Code structure:
Contains 3 functions other than main.
- print_list() is to print out the price list so that the customer can choose what they want.
Customors can also chose to have the list sorted by fruit name or by price.
If customer do not add command line argument, the list will not be sorted.
If customer use command line argument "fruit_name", the list will be sorted by fruit name in ascending order.
If customer use command line argument "price", the list will be sorted by price in ascending order.
Unexpected command line argument will print the unsorted list.
- collect_item() is asking the users to input what they want to buy. One input each time.
The programe will show what in cart and total cost every time the user input one new item.
The user can stop adding thing into cart by "Control + D".
- discount() is to generate discount between 0-50% off and calculate the final cost.

