words = set()

def check():
    return [word for word in words if len(word) > 2]


def size():
    return  len(words)

def  add_word(word):
    # Checks to see if the word is already in our dictionary. If not add it
    if word not in words:
        words.add(word)
        return True
    return  False


add_word('apple')