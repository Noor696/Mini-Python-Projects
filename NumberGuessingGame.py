import random  # random is module in python 

top_range = input("Type a Top range number: ")

# int("25") -> 25

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0 :
        print("Please type a number larger than 0 next time.")
        quit()

else:
    print("Please type a number time.")
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number time.")
        continue

    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess > random_number:
            print("You were above the number")
    else:
        print("You were bellow the number")

print("You got it in" , guesses , "guesses")
# == print("You got it in " + str(guesses) + " guesses")


# randint(10) -> take number from 0 to 10
# randrange(10) -> take number from 0 to 9

