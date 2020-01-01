./raindrops/raindrops.py

```python
def convert(number):
    drop_factors=zip([3,5,7],["Pling", "Plang", "Plong"])
    droplet=''.join([drop for factor, drop in drop_factors if (number % factor == 0) ])
    if not droplet:
        return str(number)
    else:
        return droplet 
```

./robot-name/robot_name.py
```
class Robot(object):
# Issues
# importing random from a global scope raises an error
# the .reset() method appears to work in the console, but then fails the final test in robot_name_test.py

    def __init__(self):
        import random
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.name = alphabet[random.randint(0,25)] + alphabet[random.randint(0,25)] + str(random.randint(100,999))

    def reset(self):
        self.__init__()
```
./series/series.py
```
def slices(series, length):
    slices=[]
    if len(series) == 0:  
        raise ValueError("Error: Please Input a Series")
    elif length <= 0:
        raise ValueError("Error: The Length of the Slice Can't be Less than 0")
    elif length > len(series):
        raise ValueError("Error: The Length of the Slice Can't be Greater than the Length of the Series")
    else:
        for x in range(len(series)-(length-1)):
            slices.append(series[x:x+length])
    return slices
```
./pangram/pangram.py
```
def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet=set('abcdefghijklmnopqrstuvwxyz')
    if sentence == "":
        return False 
    else:
        for c in alphabet:
            if c not in sentence:
                return False;
        return True; 
```
./high-scores/high_scores.py
```
class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.sortedScores = scores[:]
        self.sortedScores.sort(reverse = True)
    def latest (self):
        return self.scores[-1]
    def personal_best(self):
        return self.sortedScores[0]
    def personal_top_three(self):
        return self.sortedScores[0:3]
```
./simple-cipher/simple_cipher.py
```
class Cipher(object):
    def __init__(self, key):
        if key:
            self.key=key
            print("key's here")
        else:
            self.key='aaaaaaaaaaaaaaaa'
            print("No key, setting to 'aaaaaaaaaaaaaaaa'")
        self.alphabet="abcdefghijklmnopqrstuvwxyz"
        self.enc_key=[self.alphabet.index(key[n]) for n in range(len(key))]
        self.encoded=[]
        self.decoded=[]
    def encode(self, text):
        i=0
        indexed_txt=[self.alphabet.index(text[n]) for n in range(len(text))]
        print("Text indices: " + str(indexed_txt))
        print("Key indices: " + str(self.enc_key))
        for n in range(len(text)):
           if indexed_txt[n]+self.enc_key[i] < 26:
               self.encoded.append(self.alphabet[indexed_txt[n]+self.enc_key[i]])
           else:
               self.encoded.append(self.alphabet[(indexed_txt[n]+self.enc_key[i])-26])
           i=i+1
           if i > (len(self.enc_key)-1):
               i=0
        return ''.join(self.encoded)

    def decode(self, text):
        i=0
        indexed_txt=[self.alphabet.index(text[n]) for n in range(len(text))]
        print("Encoded text indices: " + str(indexed_txt))
        for n in range(len(text)):
           if indexed_txt[n]-self.enc_key[i] >= 0:
               self.decoded.append(self.alphabet[indexed_txt[n]-self.enc_key[i]])
           else:
               self.decoded.append(self.alphabet[(indexed_txt[n]-self.enc_key[i])+26])
           i=i+1
           if i > (len(self.enc_key)-1):
               i=0
        return ''.join(self.decoded)

cipher=Cipher("fakjsdfkj")
encoded=cipher.encode("chickcorea")
decoded=cipher.decode(''.join(encoded))
print(encoded)
print(decoded)

```
./hello-world/hello_world.py
```
def hello():
    return 'Hello, World!'

```
./hangman/hangman_non_list.py
```
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
```
./hangman/hangman.py
```
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
```
./matrix/matrix.py
```
class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_string = [item.split() for item in self.matrix_string.splitlines()]
        self.matrix_string = [[int(item) for item in self.matrix_string[nestedList]] for nestedList in range(len(self.matrix_string))]
    def row(self, index):
        return self.matrix_string[index-1]
    def column(self, index):
        column=[self.matrix_string[item][index-1] for item in range(len(self.matrix_string))]
        return column
```
./isogram/isogram.py
```
def is_isogram(string):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    string=''.join([i for i in string if i.isalpha()])
    alphabetical_characters=set(string.lower())
    if len(alphabetical_characters) != len(string):
        return False
    else:
        return True
```
./hamming/hamming.py
```
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are not the same length.")
    zipped=zip(strand_a, strand_b)
    difference = [(nuc_a, nuc_b) for nuc_a, nuc_b in zipped if nuc_a != nuc_b]
    return len(difference)
```
./two-fer/two_fer.py
```
def two_fer(name="you"):
    return "One for {}, one for me.".format(name)
```
./twelve-days/twelve_days.py
```
def recite(start_verse, end_verse):
        gifts=["twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        "and a Partridge in a Pear Tree."]
        if start_verse and end_verse == 1:
            gifts[11]="a Partridge in a Pear Tree."
        days=["first","second","third","fourth","fifth","sixth","seventh","eigth","ninth","tenth","eleventh", "twelfth"]
        print(("On the %s day of Christmas my true love gave to me: \n" % days[start_verse-1]) + '\n'.join(gifts[(12-start_verse):12]))

        
```
./bank-account/bank_account.py
```
class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.is_open = False
        self.closed_error = ValueError("That account is closed")
        self.insufficient =  ValueError("Insufficient funds")

    def get_balance(self):
        if self.is_open == False:
            raise ValueError("Not is_open")
        else:
            return self.balance

    def open(self):
        if self.is_open == True:
            raise ValueError("Already is_open")
        else:
            self.is_open = True
            self.balance=0

    def deposit(self, amount):
        if self.is_open == False:
            raise ValueError("That account is closed")
        elif amount < 0:
            raise ValueError("No negative amounts")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if self.is_open == False:
            raise ValueError("That account is closed")
        elif (self.balance - amount) < 0:
            raise ValueError("Insufficient funds")
        elif amount < 0:
            raise ValueError("No negative amounts")
        else:
            self.balance -= amount

    def close(self):
        if self.is_open == False:
            raise ValueError("Already closed")
        else:
            self.is_open = False
```
./raindrops/raindrops.py
```
def convert(number):
    drop_factors=zip([3,5,7],["Pling", "Plang", "Plong"])
    droplet=''.join([drop for factor, drop in drop_factors if (number % factor == 0) ])
    if not droplet:
        return str(number)
    else:
        return droplet
    
```
./robot-name/robot_name.py
```
class Robot(object):
# Issues
# importing random from a global scope raises an error
# the .reset() method appears to work in the console, but then fails the final test in robot_name_test.py

    def __init__(self):
        import random
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.name = alphabet[random.randint(0,25)] + alphabet[random.randint(0,25)] + str(random.randint(100,999))

    def reset(self):
        self.__init__()
```
./series/series.py
```
def slices(series, length):
    slices=[]
    if len(series) == 0:  
        raise ValueError("Error: Please Input a Series")
    elif length <= 0:
        raise ValueError("Error: The Length of the Slice Can't be Less than 0")
    elif length > len(series):
        raise ValueError("Error: The Length of the Slice Can't be Greater than the Length of the Series")
    else:
        for x in range(len(series)-(length-1)):
            slices.append(series[x:x+length])
    return slices
```
./pangram/pangram.py
```
def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet=set('abcdefghijklmnopqrstuvwxyz')
    if sentence == "":
        return False 
    else:
        for c in alphabet:
            if c not in sentence:
                return False;
        return True; 
```
./high-scores/high_scores.py
```
class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.sortedScores = scores[:]
        self.sortedScores.sort(reverse = True)
    def latest (self):
        return self.scores[-1]
    def personal_best(self):
        return self.sortedScores[0]
    def personal_top_three(self):
        return self.sortedScores[0:3]
```
./simple-cipher/simple_cipher.py
```
class Cipher(object):
    def __init__(self, key):
        if key:
            self.key=key
            print("key's here")
        else:
            self.key='aaaaaaaaaaaaaaaa'
            print("No key, setting to 'aaaaaaaaaaaaaaaa'")
        self.alphabet="abcdefghijklmnopqrstuvwxyz"
        self.enc_key=[self.alphabet.index(key[n]) for n in range(len(key))]
        self.encoded=[]
        self.decoded=[]
    def encode(self, text):
        i=0
        indexed_txt=[self.alphabet.index(text[n]) for n in range(len(text))]
        print("Text indices: " + str(indexed_txt))
        print("Key indices: " + str(self.enc_key))
        for n in range(len(text)):
           if indexed_txt[n]+self.enc_key[i] < 26:
               self.encoded.append(self.alphabet[indexed_txt[n]+self.enc_key[i]])
           else:
               self.encoded.append(self.alphabet[(indexed_txt[n]+self.enc_key[i])-26])
           i=i+1
           if i > (len(self.enc_key)-1):
               i=0
        return ''.join(self.encoded)

    def decode(self, text):
        i=0
        indexed_txt=[self.alphabet.index(text[n]) for n in range(len(text))]
        print("Encoded text indices: " + str(indexed_txt))
        for n in range(len(text)):
           if indexed_txt[n]-self.enc_key[i] >= 0:
               self.decoded.append(self.alphabet[indexed_txt[n]-self.enc_key[i]])
           else:
               self.decoded.append(self.alphabet[(indexed_txt[n]-self.enc_key[i])+26])
           i=i+1
           if i > (len(self.enc_key)-1):
               i=0
        return ''.join(self.decoded)

cipher=Cipher("fakjsdfkj")
encoded=cipher.encode("chickcorea")
decoded=cipher.decode(''.join(encoded))
print(encoded)
print(decoded)

```
./hello-world/hello_world.py
```
def hello():
    return 'Hello, World!'

```
./hangman/hangman_non_list.py
```
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
```
./hangman/hangman.py
```
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
```
./matrix/matrix.py
```
class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_string = [item.split() for item in self.matrix_string.splitlines()]
        self.matrix_string = [[int(item) for item in self.matrix_string[nestedList]] for nestedList in range(len(self.matrix_string))]
    def row(self, index):
        return self.matrix_string[index-1]
    def column(self, index):
        column=[self.matrix_string[item][index-1] for item in range(len(self.matrix_string))]
        return column
```
./isogram/isogram.py
```
def is_isogram(string):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    string=''.join([i for i in string if i.isalpha()])
    alphabetical_characters=set(string.lower())
    if len(alphabetical_characters) != len(string):
        return False
    else:
        return True
```
./hamming/hamming.py
```
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are not the same length.")
    zipped=zip(strand_a, strand_b)
    difference = [(nuc_a, nuc_b) for nuc_a, nuc_b in zipped if nuc_a != nuc_b]
    return len(difference)
```
./two-fer/two_fer.py
```
def two_fer(name="you"):
    return "One for {}, one for me.".format(name)
```
./twelve-days/twelve_days.py
```
def recite(start_verse, end_verse):
        gifts=["twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        "and a Partridge in a Pear Tree."]
        if start_verse and end_verse == 1:
            gifts[11]="a Partridge in a Pear Tree."
        days=["first","second","third","fourth","fifth","sixth","seventh","eigth","ninth","tenth","eleventh", "twelfth"]
        print(("On the %s day of Christmas my true love gave to me: \n" % days[start_verse-1]) + '\n'.join(gifts[(12-start_verse):12]))

        
```
./bank-account/bank_account.py
```
class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.is_open = False
        self.closed_error = ValueError("That account is closed")
        self.insufficient =  ValueError("Insufficient funds")

    def get_balance(self):
        if self.is_open == False:
            raise ValueError("Not is_open")
        else:
            return self.balance

    def open(self):
        if self.is_open == True:
            raise ValueError("Already is_open")
        else:
            self.is_open = True
            self.balance=0

    def deposit(self, amount):
        if self.is_open == False:
            raise ValueError("That account is closed")
        elif amount < 0:
            raise ValueError("No negative amounts")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if self.is_open == False:
            raise ValueError("That account is closed")
        elif (self.balance - amount) < 0:
            raise ValueError("Insufficient funds")
        elif amount < 0:
            raise ValueError("No negative amounts")
        else:
            self.balance -= amount

    def close(self):
        if self.is_open == False:
            raise ValueError("Already closed")
        else:
            self.is_open = False
```
./raindrops/raindrops.py
```
def convert(number):
    drop_factors=zip([3,5,7],["Pling", "Plang", "Plong"])
    droplet=''.join([drop for factor, drop in drop_factors if (number % factor == 0) ])
    if not droplet:
        return str(number)
    else:
        return droplet
    
```
./robot-name/robot_name.py
```
class Robot(object):
# Issues
# importing random from a global scope raises an error
# the .reset() method appears to work in the console, but then fails the final test in robot_name_test.py

    def __init__(self):
        import random
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.name = alphabet[random.randint(0,25)] + alphabet[random.randint(0,25)] + str(random.randint(100,999))

    def reset(self):
        self.__init__()
```
./series/series.py
```
def slices(series, length):
    slices=[]
    if len(series) == 0:  
        raise ValueError("Error: Please Input a Series")
    elif length <= 0:
        raise ValueError("Error: The Length of the Slice Can't be Less than 0")
    elif length > len(series):
        raise ValueError("Error: The Length of the Slice Can't be Greater than the Length of the Series")
    else:
        for x in range(len(series)-(length-1)):
            slices.append(series[x:x+length])
    return slices
```
./pangram/pangram.py
```
def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet=set('abcdefghijklmnopqrstuvwxyz')
    if sentence == "":
        return False 
    else:
        for c in alphabet:
            if c not in sentence:
                return False;
        return True; 
```
./high-scores/high_scores.py
```
class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.sortedScores = scores[:]
        self.sortedScores.sort(reverse = True)
    def latest (self):
        return self.scores[-1]
    def personal_best(self):
        return self.sortedScores[0]
    def personal_top_three(self):
        return self.sortedScores[0:3]
```
./simple-cipher/simple_cipher.py
```
class Cipher(object):
    def __init__(self, key):
        if key:
            self.key=key
            print("key's here")
        else:
            self.key='aaaaaaaaaaaaaaaa'
            print("No key, setting to 'aaaaaaaaaaaaaaaa'")
        self.alphabet="abcdefghijklmnopqrstuvwxyz"
        self.enc_key=[self.alphabet.index(key[n]) for n in range(len(key))]
        self.encoded=[]
        self.decoded=[]
    def encode(self, text):
        i=0
        indexed_txt=[self.alphabet.index(text[n]) for n in range(len(text))]
        print("Text indices: " + str(indexed_txt))
        print("Key indices: " + str(self.enc_key))
        for n in range(len(text)):
           if indexed_txt[n]+self.enc_key[i] < 26:
               self.encoded.append(self.alphabet[indexed_txt[n]+self.enc_key[i]])
           else:
               self.encoded.append(self.alphabet[(indexed_txt[n]+self.enc_key[i])-26])
           i=i+1
           if i > (len(self.enc_key)-1):
               i=0
        return ''.join(self.encoded)

    def decode(self, text):
        i=0
        indexed_txt=[self.alphabet.index(text[n]) for n in range(len(text))]
        print("Encoded text indices: " + str(indexed_txt))
        for n in range(len(text)):
           if indexed_txt[n]-self.enc_key[i] >= 0:
               self.decoded.append(self.alphabet[indexed_txt[n]-self.enc_key[i]])
           else:
               self.decoded.append(self.alphabet[(indexed_txt[n]-self.enc_key[i])+26])
           i=i+1
           if i > (len(self.enc_key)-1):
               i=0
        return ''.join(self.decoded)

cipher=Cipher("fakjsdfkj")
encoded=cipher.encode("chickcorea")
decoded=cipher.decode(''.join(encoded))
print(encoded)
print(decoded)

```
./hello-world/hello_world.py
```
def hello():
    return 'Hello, World!'

```
./hangman/hangman_non_list.py
```
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
```
./hangman/hangman.py
```
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
```
./matrix/matrix.py
```
class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_string = [item.split() for item in self.matrix_string.splitlines()]
        self.matrix_string = [[int(item) for item in self.matrix_string[nestedList]] for nestedList in range(len(self.matrix_string))]
    def row(self, index):
        return self.matrix_string[index-1]
    def column(self, index):
        column=[self.matrix_string[item][index-1] for item in range(len(self.matrix_string))]
        return column
```
./isogram/isogram.py
```
def is_isogram(string):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    string=''.join([i for i in string if i.isalpha()])
    alphabetical_characters=set(string.lower())
    if len(alphabetical_characters) != len(string):
        return False
    else:
        return True
```
./hamming/hamming.py
```
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are not the same length.")
    zipped=zip(strand_a, strand_b)
    difference = [(nuc_a, nuc_b) for nuc_a, nuc_b in zipped if nuc_a != nuc_b]
    return len(difference)
```
./two-fer/two_fer.py
```
def two_fer(name="you"):
    return "One for {}, one for me.".format(name)
```
./twelve-days/twelve_days.py
```
def recite(start_verse, end_verse):
        gifts=["twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        "and a Partridge in a Pear Tree."]
        if start_verse and end_verse == 1:
            gifts[11]="a Partridge in a Pear Tree."
        days=["first","second","third","fourth","fifth","sixth","seventh","eigth","ninth","tenth","eleventh", "twelfth"]
        print(("On the %s day of Christmas my true love gave to me: \n" % days[start_verse-1]) + '\n'.join(gifts[(12-start_verse):12]))

        
```
./bank-account/bank_account.py
```
class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.is_open = False
        self.closed_error = ValueError("That account is closed")
        self.insufficient =  ValueError("Insufficient funds")

    def get_balance(self):
        if self.is_open == False:
            raise ValueError("Not is_open")
        else:
            return self.balance

    def open(self):
        if self.is_open == True:
            raise ValueError("Already is_open")
        else:
            self.is_open = True
            self.balance=0

    def deposit(self, amount):
        if self.is_open == False:
            raise ValueError("That account is closed")
        elif amount < 0:
            raise ValueError("No negative amounts")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if self.is_open == False:
            raise ValueError("That account is closed")
        elif (self.balance - amount) < 0:
            raise ValueError("Insufficient funds")
        elif amount < 0:
            raise ValueError("No negative amounts")
        else:
            self.balance -= amount

    def close(self):
        if self.is_open == False:
            raise ValueError("Already closed")
        else:
            self.is_open = False
```
