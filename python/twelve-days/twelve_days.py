gifts=['two Turtle Doves',
 'three French Hens',
 'four Calling Birds',
 'five Gold Rings',
 'six Geese-a-Laying',
 'seven Swans-a-Swimming',
 'eight Maids-a-Milking',
 'nine Ladies Dancing',
 'ten Lords-a-Leaping',
 'eleven Pipers Piping',
 'twelve Drummers Drumming']
days=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh", "twelfth"]
verse="On the {} day of Christmas my true love gave to me: {}{}"
def recite(start_verse, end_verse):
    return [format_verse(n) for n in range(start_verse, end_verse+1)]
def format_verse(n):
    return verse.format(
                days[n-1],
                ', '.join(gifts[n-2::-1]) if n > 1 else "",
                ", and a Partridge in a Pear Tree." if n > 1 else "a Partridge in a Pear Tree."
    )
