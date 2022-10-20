# O(N*2^N) time | O(N) space
# max recursive depth, store all nodes in temp
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        output = []

        def dfs(idx, temp):
            temp.append(idx)

            if idx == len(graph) - 1:
                output.append(temp[:])
                return

            for num in graph[idx]:
                dfs(num, temp)
                temp.pop()


        dfs(0, [])

        return output
