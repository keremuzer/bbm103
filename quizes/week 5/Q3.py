import random


def guessing_game():
    number = random.randint(1, 10)
    guess = 0
    while guess != number:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < number:
            print("increase your number")
        elif guess > number:
            print("decrease your number")
    print(f"You guessed the number {number} correctly!")


guessing_game()
