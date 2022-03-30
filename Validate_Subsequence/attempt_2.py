# O(n) time, O(1) space - where n is length of array

def isValidSubsequence(array, sequence):
    check = 0
    for num in array:
        if check == len(sequence):
            break
        if sequence[check] == num:
            check += 1
    return check == len(sequence)
