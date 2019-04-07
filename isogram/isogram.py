import re


def is_isogram(string):
    filtered_string = re.sub("[^a-z]", "", string.lower())
    return len(set(filtered_string)) == len(filtered_string)
