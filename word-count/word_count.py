import collections
import re


def word_count(phrase):
    phrase = phrase.lower()
    # all symbols except '0-9a-zA-Z | apostrophes in the end | apostrophes at the beginning
    filtered_phrase = re.sub('[^\'0-9a-zA-Z]|\'(?![a-z])|(?<![a-z])\'', ' ', phrase)
    words = filter(None, re.split("\s+", filtered_phrase))

    c = collections.Counter(words)
    return dict(c)


