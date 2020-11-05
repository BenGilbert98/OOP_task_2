from values import ScrabbleLetters

word = input("What is your word?   ").lower() # takes the word input and makes it lower case

print(f"Your word is {word} and scored {ScrabbleLetters(word).wordscore()} points") # shows your word and its point value
