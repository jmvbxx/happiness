# This this program does two things:
#
# 1. Create a dictionary based on the happiness word list (AFINN-111.txt)
# 2. Prompts the user to choose a word and returns the value of that word

import re

words_dict = {}

# Generate dictionary from word list
with open("AFINN-111.txt") as words:
    for line in words:
        word, score = line.strip().split("\t")
        words_dict[word] = int(score)

print("This will return the 'happiness' value of a word!")
while True:
    happy_word = raw_input("Please enter a word: ")

    try:
        if any(letter.isdigit() for letter in happy_word):
            raise ValueError()
        print words_dict[happy_word]
        break
    except KeyError:
        print("That word doesn't have a 'happiness' rating.")
    except ValueError:
        print("Nice try! That's not a word")