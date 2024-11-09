import random


sum_of_even_digits = 0
sum_of_odd_digits = 0


credit_card_number = input("What is the card number: ")
credit_card_number = credit_card_number.replace(" ", "")
credit_card_number = credit_card_number.replace("-", "")
credit_card_number = credit_card_number[::-1]

for numbers in credit_card_number[::2]:
    sum_of_odd_digits += int(numbers)

for numbers in credit_card_number[1::2]:
    numbers = int(numbers) * 2
    if numbers > 10:
        sum_of_even_digits += (1 + (numbers % 10))
    else: 
        sum_of_even_digits += numbers


total = sum_of_even_digits + sum_of_odd_digits

if total % 10 == 0:
    print("Valid card.")
else:
    print("Invalid card.")
