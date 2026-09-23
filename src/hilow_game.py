"""TODO: Replace with a one-line summary of the optional practice program.

Input:
    TODO: Identify the major user inputs.

Process:
    TODO: Summarize validation, random selection, decisions, and
    repetition from your pseudocode.

Output:
    TODO: Identify the major categories of console output.
"""

# === Imports ===
from random import randint


# === Main Function ===
def main() -> None:
    """Run the optional higher/lower game practice program."""

            lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))

    while lower >= upper:
        print("Invalid bounds. The lower bound must be less than the upper bound.")
        lower = int(input("Enter the lower bound: "))
        upper = int(input("Enter the upper bound: "))

    number = randint(lower, upper)

    guess = int(input(f"Guess a number from {lower} to {upper}: "))

    while guess != number:
        if guess < lower or guess > upper:
            print("Invalid guess. Enter a number within the valid range.")
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")

        guess = int(input(f"Guess a number from {lower} to {upper}: "))

    print("Congratulations! You guessed the correct number.")

    


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Add an APA-style reference for a source you used, or delete this line.
