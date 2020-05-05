an_letters = "aeiouhfsrnAEIOUHFSRN"
word = input("Enter a word: ")
times = int(input("Whats your enthusiasm level out 10 :"))

for char in word:
    if char in an_letters:
        print("give me an " + char + "!" + char)
    else:
        print("Give me a " + char + "!" + char)

print("What does that read!! ")
for i in range(times):
   print(word)