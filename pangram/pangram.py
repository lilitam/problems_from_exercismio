import string
def is_pangram(sentence):
    cleanlist = []
    sentence = sentence.lower()
    for i in sentence:
        if i not in cleanlist and i in string.ascii_lowercase:
            cleanlist.append(i)

    len_cleanlist = len(cleanlist)
    len_alphabet = len(string.ascii_lowercase)
    if len_cleanlist == len_alphabet:
        return True
    else:
        return False
    pass
