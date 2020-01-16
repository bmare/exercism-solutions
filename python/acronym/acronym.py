def abbreviate(words):
    stripped=''.join([ch if ch.isalnum() or ch == "'" or ch.isspace() else " " for ch in words])
    return ''.join([word[0].upper() for word in stripped.split()])
