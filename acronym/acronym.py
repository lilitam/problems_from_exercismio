import re


def abbreviate(words):
    words = re.sub(r"[-_0-9]", " ", words)
    splitted_words = list(words.split())
    acronym = ''.join([w[0] for w in splitted_words])
    return acronym.upper()
