secret_num = 7
num_guesses = 0
guess_limit = 3
while num_guesses < guess_limit:
    guess = int(input("Guess: "))
    num_guesses += 1
    if guess == secret_num:
        print("You won!")
        break
else:
    print("You Lost Try Again")
