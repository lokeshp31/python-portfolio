import random

def main():
    print("=== Number Guessing Game ===")
    secret = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number (1-100): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        attempts += 1
        if guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
