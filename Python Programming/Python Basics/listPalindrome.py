palinList = []
maxLen = 0
maxWord = ""

while True:
    word = input("Enter a word: ")
    if word == word[::-1]:
        palinList.append(word)
        if len(word) > maxLen:
            maxLen = len(word)
            maxWord = word
    choice = input("Do you want to enter more word?(Y/N)")
    if choice.upper() == 'Y':
        continue
    elif choice.upper() == 'N':
        break    

print(f"Longest word is {maxWord} and its length is {maxLen}")

