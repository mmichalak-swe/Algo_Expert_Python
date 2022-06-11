# Not a valid solution due to question constraints
# not an optimal time complexity
def multiStringSearch(bigString, smallStrings):
    output = [False for _ in smallStrings]
    for i, little in enumerate(smallStrings):
        if little in bigString:
            output[i] = True
    return output
