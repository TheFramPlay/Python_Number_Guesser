import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0
score = 10
print("You start with 10 points!")

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess >random_number:
        score -= 1
        print('You\'re guess was too high!')
        print("Score:", score)
    else:
        score -= 1
        print('You\'re guess was too low!')
        print("Score:", score)

print("You got it in", guesses, "guesses")
print("Score:", score)

