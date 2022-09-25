# O(N) time | O(1) space, where N is the number of elements (n*n)
def findCircleNum(isConnected):

    def dfsHelper(city, cities):
        # already visited, or no connection, return
        if isConnected[city][city] == 0:
            return
        for connection in range(cities):
            # if 1, we haven't visited
            if isConnected[city][connection] == 1:
                isConnected[city][connection] = 0
                dfsHelper(connection, cities)
    
    
    provinces = 0
    cities = len(isConnected)
    
    for i in range(cities):
        if isConnected[i][i]:
            provinces += 1
            dfsHelper(i, cities)
    
    return provinces
