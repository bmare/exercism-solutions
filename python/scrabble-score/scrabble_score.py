def score(word):
    total=0
    score_dict={("A", "E", "I", "O", "U", "L","N", "R", "S", "T"): 1, ("D","G"):2, ("B","C","M","P"):3,("F","H","V","W","Y"):4, ("F","H","V","W","Y"):4, ("K"):5, ("J","X"):8, ("Q","Z"):10} 
    for ch in word.upper():
        for key in score_dict.keys():
            if ch in key:
                total+=score_dict.get(key,0)
    return total
