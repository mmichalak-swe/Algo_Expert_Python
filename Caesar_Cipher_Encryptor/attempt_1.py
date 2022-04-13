def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    workable = [x for x in string]

    for i, char in enumerate(workable):
        idx = alphabet.index(char)
        idx += key
        while idx > 25:
            idx -= 26
        workable[i] = alphabet[idx]
    return "".join(workable)
