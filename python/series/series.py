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
