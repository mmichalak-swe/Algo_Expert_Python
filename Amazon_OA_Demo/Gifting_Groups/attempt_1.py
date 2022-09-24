def countGroups(related):
    num = 0
    people = len(related)
    related = [[int(char) for char in row] for row in related]
    
    for i in range(people):
        if related[i][i] == 1:
            num += 1
            dfsHelper(i, people, related)
    return num

def dfsHelper(idx, people, related):
    if related[idx][idx] == 0:
        return
    for i in range(people):
        if related[idx][i] == 1:
            related[idx][i] = 0
            dfsHelper(i, people, related)
