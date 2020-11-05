from values import ScrabbleLetters

word = input("What is your word?   ").lower()

print(f"Your word is {word} and scored {ScrabbleLetters(word).wordscore()} points")
