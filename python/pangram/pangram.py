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
