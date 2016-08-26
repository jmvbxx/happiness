# This this program does two things:
#
# 1. Create a dictionary based on the happiness word list (AFINN-111.txt)
# 2. Prompt you choose between list all the words with a certain value
#    or write a word and get it's happiness score.

import re

words = open("AFINN-111-short.txt").readlines()

words_dict = {}

# Generate dictionary from word list
for line in words:
	entry = line.strip().split("\t")
	word = entry[0]
	score = entry[1]
	words_dict[word] = int(score)

print("This will return the 'happiness' value of a word!")
happy_word = raw_input("Please enter a word: ")

if re.match(r"^[a-zA-Z0-9]+$", happy_word):
	if words_dict.has_key(happy_word):
		print words_dict[happy_word]
	else:
		print("That word doesn't have a 'happiness' rating.")
else:
	print("Nice try! That's not a word")