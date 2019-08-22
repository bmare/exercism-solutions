# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word=word
        self.masked_word= ['_' for ch in range(len(self.word))]
    def guess(self, char):
        if self.status==STATUS_LOSE or self.status==STATUS_WIN:
             raise ValueError('The game is already over.')
        elif char in self.word and char not in self.masked_word:
            for ch in range(len(self.word)):
                if self.word[ch]==char:
                    self.masked_word[ch]=char
        else: 
                self.remaining_guesses=self.remaining_guesses - 1
    def get_masked_word(self):
        return ''.join(self.masked_word)
    def get_status(self):
        if "_" not in self.masked_word:
            self.status = STATUS_WIN
        elif self.remaining_guesses <= 0:
            self.status = STATUS_LOSE
        return self.status
