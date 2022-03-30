def isValidSubsequence(array, sequence):
    
    for num in array:
        if num == sequence[0]:
            sequence.pop(0)
            if not sequence:
                return True
	
    return sequence == []
