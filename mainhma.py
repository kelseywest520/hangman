import random

open_file = open("/usr/share/dict/words")
contents = open_file.read()
open_file.close()

word = contents.split("\n")
word = random.choice (word)
max_wrong= len(word) - 1
blanks= "_" * len(word)



while True:
    print("Guess a letter.")
    word= input()
    guess = guess.lower()
