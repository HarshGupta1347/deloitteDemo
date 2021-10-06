# WAP to check if number entered by the user is palindrome or perfect number based on user choice

choice = input("Please select option \nSelect 1 for Palindrome\nSelect 2 for Perfect\n")
number = int(input("Input number to be checked: "))
if choice == "1":
    if str(number) == str(number)[::-1]:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")
if choice == "2":
    divisors = []
    for i in range(1,number):
        if number % i == 0:
            divisors.append(i)
    if sum(divisors) == number:
        print("Perfect Number")
    else:
        print("Not a perfect number")
