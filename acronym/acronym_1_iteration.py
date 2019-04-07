import string


def abbreviate(words):
    words = words.lower()
    splitted_words = words.split()
    acronym = ""
    for w in splitted_words:
        # if word doesn't contain ascii letters
        index = 0
        while index < len(w) and w[index] not in string.ascii_lowercase:
            index += 1

        if index == len(w):
            continue

        acronym += w[index]

        # if word contains hyphen
        if "-" in w:
            splitted_w = w.split("-")
            acronym += splitted_w[1][0]

    return acronym.upper()