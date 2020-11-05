class ScrabbleLetters:

    def __init__(self, word):
        self.value_1 = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']
        self.value_2 = ['d', 'g']
        self.value_3 = ['b', 'c', 'm', 'p']
        self.value_4 = ['f', 'h', 'v', 'w', 'y']
        self.value_5 = ['k']
        self.value_8 = ['j', 'x']
        self.value_10 = ['q', 'z']
        self.word = word

    def wordscore(self):
        score = 0
        letters = self.word
        for i in letters:
            if i in self.value_1:
                score += 1
            elif i in self.value_2:
                score += 2
            elif i in self.value_3:
                score += 3
            elif i in self.value_4:
                score += 4
            elif i in self.value_5:
                score += 5
            elif i in self.value_8:
                score += 8
            elif i in self.value_10:
                score += 10
        return score
