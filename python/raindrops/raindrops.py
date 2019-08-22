def convert(number):
    drop_factors=zip([3,5,7],["Pling", "Plang", "Plong"])
    droplet=''.join([drop for factor, drop in drop_factors if (number % factor == 0) ])
    if not droplet:
        return str(number)
    else:
        return droplet
    
