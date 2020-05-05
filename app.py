an_letters = "aehislofmnrxAEHISLOFMNRX"
word = input("enter a word...ill cheer for you : ")
times = int(input("whats your enthusiasm level between 1 - 10 : "))


for char in word:
    if char in an_letters:
        print("give me an " + char + " ! " + char + " !")
    else:
        print("give me a " + char + "  ! " + char + " !")
print("the word is!")
for i in range(times):
    print(word)
