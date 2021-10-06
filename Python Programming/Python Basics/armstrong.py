# WAP to check if number is an Armstrong Number or not

number = input("Enter a number to be checked: ")
sum_of_number = 0
for i in number:
    sum_of_number += int(i)**3
if sum_of_number == int(number):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")