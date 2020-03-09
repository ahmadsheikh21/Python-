import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("Guess the Number between 20 :"))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number is larger than the Original Number")
        elif guess < to_be_guessed:
            print("Number is smaller than the original number")
    else:
                       print("Sorry You Lost")
                       break

else:
        print("Congratulation you won ")
        

