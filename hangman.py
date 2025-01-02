import random
import numpy as np
import matplotlib.pyplot as plt

class Hangman:
    def __init__(self, old_filename, new_filename):
        self.old_filename = old_filename
        self.new_filename = new_filename
        data = np.genfromtxt(old_filename, dtype=str, delimiter="\n")
        self.categories = {}
        for line in data:
            category, words = line.split("\t")
            self.categories[category] = words.split(", ")
        self.category = np.random.choice(list(self.categories.keys()))
        self.word = np.random.choice(self.categories[self.category])
        self.guessed_letters = []
        self.remaining_tries = 6
        self.correct_guesses = 0
        self.incorrect_guesses = 0

    def reset_game(self):
        self.category = np.random.choice(list(self.categories.keys()))
        self.word = np.random.choice(self.categories[self.category])
        self.guessed_letters = []
        self.remaining_tries = 6

    def display_word(self):
        display = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += '_'
        return display

    def make_guess(self, letter):
        if self.remaining_tries > 0:
            if letter.isalpha() and len(letter) == 1:
                letter = letter.lower()
                if letter not in self.guessed_letters:
                    self.guessed_letters.append(letter)
                    if letter not in self.word:
                        self.remaining_tries -= 1
                        self.incorrect_guesses += 1
                    else:
                        self.correct_guesses += 1
                    return True
        return False

    def check_win(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def add_category(self, category, words):
        if category in self.categories:
            self.categories[category].extend(words)
        else:
            self.categories[category] = words

    def save_to_new_file(self):
        with open(self.new_filename, "w") as new_file:
            for category, words in self.categories.items():
                new_file.write(f"{category}\t{', '.join(words)}\n")

    def play(self):
        while True:
            self.reset_game()
            while self.remaining_tries > 0 and not self.check_win():
                print(f"\nCategory: {self.category}")
                print(f"Word: {self.display_word()}")
                print("Used letters:", ', '.join(self.guessed_letters))
                print("Remaining tries:", self.remaining_tries)
                guess = input("Enter a letter: ").strip()
                if self.make_guess(guess):
                    if self.check_win():
                        print(f"\nCongratulations! You won! The word was: {self.word}")
                        break
                else:
                    print("Please enter a valid unused letter")
            if self.remaining_tries == 0:
                print(f"\nGame Over! The word was: {self.word}")
            self.plot_results()
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing Hangman! Goodbye!")
                break


    def plot_results(self):
        categories = ['Correct Guesses', 'Incorrect Guesses']
        values = [self.correct_guesses, self.incorrect_guesses]
        plt.bar(categories, values, color=['green', 'red'])
        plt.xlabel('Guess Type')
        plt.ylabel('Number of Guesses')
        plt.title('Hangman Guess Statistics')
        plt.show()

filename_old = "oldfile.txt"
filename_new = "newfile.txt"
game = Hangman(filename_old, filename_new)
game.add_category("Fruits", ["apple", "banana", "orange", "grape", "pear", "cherry", "fig", "kiwi", "watermelon", "blueberry"])
game.save_to_new_file()
game.play() 
