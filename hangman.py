# JT Hangman Assignment


import os
import random

MAX_WRONG = 6 


def read_words(filename):
    print(f"Loading word list from {filename}...")
    with open(filename, "r") as file:
        words = []
        for line in file:
            word = line.strip().strip('"').strip("'").upper()
            if word:
                words.append(word)
    return words


def load_stats(filename):
    try:
        with open(filename, "r") as file:
            wins = int(file.readline().strip())
            losses = int(file.readline().strip())
    except FileNotFoundError:
        wins = 0
        losses = 0
    except ValueError:
        wins = 0
        losses = 0

    print(f"Loading stats from {filename}... (Wins: {wins}, Losses: {losses})")
    return wins, losses


def save_stats(filename, wins, losses):
   
    with open(filename, "w") as file:
        file.write(str(wins) + "\n")
        file.write(str(losses) + "\n")


def show_display_word(secret_word, guessed_letters):
    
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word = display_word + letter + " "
        else:
            display_word = display_word + "_ "
    return display_word.strip()


def play_one_game(secret_word):
    guessed_letters = []
    wrong_guesses = 0

    while True:
        print()
        print("Word:", show_display_word(secret_word, guessed_letters))
        if len(guessed_letters) == 0:
            print("Guessed letters: (none yet)")
        else:
            print("Guessed letters:", ", ".join(guessed_letters))
        print("Wrong guesses remaining:", MAX_WRONG - wrong_guesses)

        
        all_found = True
        for letter in secret_word:
            if letter not in guessed_letters:
                all_found = False
        if all_found:
            print()
            print("Congratulations! You guessed the word:", secret_word)
            return True

        
        if wrong_guesses >= MAX_WRONG:
            print()
            print("Out of guesses. The word was:", secret_word)
            return False

        guess = input("Guess a letter: ").strip().upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed", guess + ". That does not cost an attempt.")
            continue

        guessed_letters.append(guess)
        if guess in secret_word:
            print("Nice!", guess, "is in the word.")
        else:
            wrong_guesses = wrong_guesses + 1
            print("Sorry,", guess, "is not in the word.")


def main():
    
    words = read_words("words.txt")
    wins, losses = load_stats("stats.txt")

    secret_word = random.choice(words)
    won = play_one_game(secret_word)

    if won:
        wins = wins + 1
    else:
        losses = losses + 1

    save_stats("stats.txt", wins, losses)
    print()
    print("Updated Stats — Wins:", wins, "Losses:", losses)


if __name__ == "__main__":
    main()
