def score(word):
    letter_sets=[("A", "E", "I", "O", "U", "L","N", "R", "S", "T"),
            ("D","G"),
            ("B","C","M","P"),
            ("F","H","V","W","Y"),
            ("K"), ("J","X"), ("Q","Z")]
    values=[1,2,3,4,5,8,10]
    score_dict={letter_sets[x][y]:values[x] \
            for x in range(len(letter_sets)) \
            for y in range(len(letter_sets[x]))} 
    return sum(score_dict.get(ch,0) for ch in word.upper())
