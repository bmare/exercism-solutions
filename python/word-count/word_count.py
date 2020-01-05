def count_words(sentence):
    count={}
    stripped=''.join([ch if ch.isalnum() or ch=="'" else " " for ch in sentence.lower()]).split()
    for word in stripped:
        word=word.strip("'")
        count[word]=count.get(word,0)+1
    return count
