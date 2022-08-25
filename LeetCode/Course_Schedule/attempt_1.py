def canFinish(numCourses, prerequisites):
    preMap = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        preMap[course].append(prereq)

    
    def dfsStateHelper(preMap, startIdx, dfsState):
        if dfsState[startIdx] == 0:
            dfsState[startIdx] = 1
        elif dfsState[startIdx] == 1:
            return True
        elif dfsState[startIdx] == 2:
            return

        for num in preMap[startIdx]:
            check = dfsStateHelper(preMap, num, dfsState)
            if check:
                return True

        dfsState[startIdx] = 2

        return False


    dfsState = [0 for num in range(len(preMap))]
    for i in range(len(dfsState)):
        if dfsState[i] == 0:
            if dfsStateHelper(preMap, i, dfsState):
                return False
    return True
