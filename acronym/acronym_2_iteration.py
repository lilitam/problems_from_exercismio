import re


def abbreviate(words):
    words = words.lower()
    words = re.sub(r"[-_0-9]", " ", words)
    splitted_words = list(words.split())
    acronym = []
    for w in splitted_words:
        acronym.append(w[0])

    acronym = "".join(acronym)
    return acronym.upper()
