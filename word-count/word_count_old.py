import re


def word_count(phrase):
    phrase = phrase.lower()
    # all symbols except '0-9a-zA-Z | apostrophes in the end | apostrophes at the beginning
    filtered_phrase = re.sub('[^\'0-9a-zA-Z]|\'(?![a-z])|(?<![a-z])\'', ' ', phrase)
    words = filter(None, re.split("\s+", filtered_phrase))
    dict_occurrences = {}
    # for i in words:
    #     if i not in dict_occurrences :
    #         dict_occurrences [i] = 1
    #     else:
    #         dict_occurrences [i] += 1
    # return dict_occurrences
    for i in words:
        dict_occurrences[i] = dict_occurrences.get(i, 0) + 1
    return dict_occurrences
