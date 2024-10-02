def rev_str(text):
    if len(text) == 1:
        return text
    return rev_str(text[1:]) + text[0]


print(rev_str("language"))
