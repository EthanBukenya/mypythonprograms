secrete_word = "Achieve"
guess = ""
guess_count = 0
out_of_guesses = False
guess_limit = 3

while guess != secrete_word:
    if guess_count < guess_limit:
      guess = input("Enter a guess :")
      guess_count += 1

    else:
        out_of_guesses = True
if out_of_guesses:
    print("Oops! Your out ouf guesses, you loose!")
elif guess_count <= 2:
    print("Congragulations .. You win Sooner, than system intended!")
else:
    print("Congrats, You still win!")


