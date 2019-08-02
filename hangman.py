import random
words = ["algorithm", "entertainment"]

words = random.choice(words)
print(words)
words = words.lower()

current_words = ["_", "_", "_", "_", "_", "_", "_", "_"] # TIP: the number of letters should match the word
print(current_words)

guesses = []
maxfails = 6
fails = 0

print(guesses)

while fails < maxfails:
	guess = input("guess one letter in the alphabet: ")
    fails = fails+1
	print("you have " + str(maxfails - fails) + " tries left!")
