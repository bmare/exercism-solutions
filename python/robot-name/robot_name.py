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
