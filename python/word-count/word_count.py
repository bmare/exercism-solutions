def count_words(sentence):
    count={}
    undesireables=['!', '&', '@', '$', '%', '^', '&', ',', '.',':','_']
    for word in sentence.lower().split():
        word=''.join([n for n in word if n not in undesireables]) 
        if word.startswith("'"):
            word=word[1:-1]
        count.setdefault(word, 0)
        count[word]=count[word]+1
    return count 

