def generateDocument(characters, document):
    letters = {}
    
    for char in characters:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    for char in document:
        if char not in letters:
            return False
        elif letters[char] == 0:
            return False
        else:
            letters[char] -= 1

    return True
