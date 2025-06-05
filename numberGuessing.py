import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    print("🎯 Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 10")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        if guess < number_to_guess:
            print("🔽 Too low!")
        elif guess > number_to_guess:
            print("🔼 Too high!")
        else:
            print("✅ You guessed it right!")
            break

if __name__ == "__main__":
    guess_number()
