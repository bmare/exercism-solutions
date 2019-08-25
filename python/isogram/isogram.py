def is_isogram(string):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    string=''.join([i for i in string if i.isalpha()])
    alphabetical_characters={ch for ch in string.lower() if ch in alphabet}
    if len(alphabetical_characters) != len(string):
        return False
    else:
        return True
