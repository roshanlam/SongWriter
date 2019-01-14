def unkify(string, vocab):
    words = string.split()
    for i, word in enumerate(words):
        if word not in vocab:
            words[i] = '*UNK*'

    return ' '.join(words)