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
        self.masked_word=""
        for ch in range(len(self.word)):
            self.masked_word+="_"
    def guess(self, char):
        if char in self.word:
            for ch in range(len(self.word)):
                if self.word[ch]==char:
                    self.masked_word[ch:] + char
            self.remaining_guesses=self.remaining_guesses - 1
        else:
            self.remaining_guesses=self.remaining_guesses - 1

    def get_masked_word(self):
        return self.masked_word
    def get_status(self):
        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
        elif "_" not in self.word:
            self.status = STATUS_WIN
        else:
            self.status = STATUS_ONGOING
        return self.status
