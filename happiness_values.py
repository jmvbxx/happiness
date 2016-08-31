# This this program does two things:
#
# 1. Create a dictionary based on the happiness word list (AFINN-111.txt)
# 2. Prompt you choose between list all the words with a certain value
#    or write a word and get it's happiness score.

words_dict = {}

# Generate dictionary from word list
with open("AFINN-111.txt") as words:
    for line in words:
        word, score = line.strip().split("\t")
        words_dict[word] = int(score)

print("This will return all the words with a specified 'happiness' value.")
while True:
    happy_value = raw_input("Please enter a 'happiness' value between -5 and 5: ")

    try:
        if int(happy_value) < -5 or 5 < int(happy_value):
            raise ValueError()
        print
        break
    except ValueError:
        print("The number you selected is outside the allowed range")