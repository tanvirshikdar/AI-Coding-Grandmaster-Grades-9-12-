import random


LOWER_BOUND = 1
UPPER_BOUND = 10
MAX_ATTEMPTS = 12

secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)


def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {LOWER_BOUND} and {UPPER_BOUND}: "))
            
            if LOWER_BOUND <= guess <= UPPER_BOUND:
                return guess
            
            print("Invalid input. Please enter a number within the specified range.")
        except ValueError:
            print("Please enter a valid integer.")


def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"


def play_game():
    attempts = 0
    won = False

    while attempts < MAX_ATTEMPTS:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "Correct":
            print(f"Congratulations! You guessed the secret number {secret_number} "
                  f"in {attempts} attempts.")
            won = True
            break
        
        print(f"{result}. Try again!")

    if not won:
        print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    play_game()