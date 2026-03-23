import random

print("🎮 Welcome to Guess the Number Game!")

# Computer chooses a random number
number = random.randint(1, 50)

# Total chances using for loop
for attempt in range(5):
    print(f"\nAttempt {attempt + 1} of 5")

    # while loop for valid input
    while True:
        guess = input("Enter a number between 1 and 50: ")

        try:
            guess = int(guess)

            if 1 <= guess <= 50:
                break
            else:
                print("⚠️ Number must be between 1 and 50!")

        except ValueError:
            print("❌ Please enter a valid number!")

    # Check guess
    if guess == number:
        print("🎉 Correct! You won!")
        break
    elif guess < number:
        print("📉 Too low!")
    else:
        print("📈 Too high!")

else:
    print(f"\n😢 Game Over! The number was {number}")