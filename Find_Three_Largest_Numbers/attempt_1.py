def findThreeLargestNumbers(array):
    highest = []
    
    for num in array:
        if len(highest) < 3:
            highest.append(num)
        
        else:
            highest.sort()
            for i in range(3):
                if num > highest[i]:
                    highest[i] = num
                    break
    highest.sort()	
    return highest
