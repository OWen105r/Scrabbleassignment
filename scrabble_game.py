"""Module providing a function printing python version."""

import random
import time

# Dictionary to store the letter values for Scrabble
letter_values = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}


# Function to calculate the Scrabble score for a given word
def scrabble_score(word):
    """Function scrabble score."""
    if not word.isalpha():
        return 0
    score = 0
    for letter in word.upper():
        if letter in letter_values:
            score += letter_values[letter]
    return score


# Function to generate a random word length between 3 and 10
def get_word_length():
    """Function get word length ."""
    return random.randint(3, 10)


# Main function to run the Scrabble game
def main():
    """Main function."""
    total_score = 0
    rounds = 0

    # Loop for 10 rounds or until the player quits
    while rounds < 10:
        word_length = get_word_length()
        print(f"Please enter a word with {word_length} letters within 15 seconds:")

        start_time = time.time()
        word = input()
        end_time = time.time()

        # Check if the entered word has the correct length
        if len(word) != word_length:
            print(f"Invalid word length. Please enter a word with exactly {word_length} letters.")
            continue

        # Check if the entered word contains only alphabets
        if not word.isalpha():
            print("Invalid input. Please enter a valid word.")
            continue

        # Calculate the time taken to enter the word
        time_taken = end_time - start_time

        # Check if the word was entered within the time limit
        if 30 > time_taken > 15:
            print("Time's up! Please enter the word faster next time.")
            continue

        # Calculate the score for the entered word
        score = scrabble_score(word)

        # Calculate the score entered and add bonus points based on the time taken
        bonus = max(0, int(15 - time_taken))  # Bonus points for faster input
        total_score += score + int(bonus)
        rounds += 1
        print(f"Score for this word: {score}")
        print(f"Bonus for fast input: {int(bonus)}")
        print(f"Total score: {total_score}")

        # Ask the player if they want to continue or quit
        continue_game = 'yes'
        if time_taken > 15:
            continue_game = input("You have taken longer than expected. We thought you quit. Do you want to continue? (yes/no): ").strip().lower()
        if continue_game != 'yes':
            print('You did not type "yes" correctly. The game thinks you put "no". You have quitted the game. Thanks for playing')
            break

    # Display the total score at the end of the game
    print(f"Game over! Your total score is {total_score}")


if __name__ == '__main__':
    main()

# This is a new line that ends the file.
