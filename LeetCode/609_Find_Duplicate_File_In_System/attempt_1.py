# O(n) time | O(n) space, where n is the number of files in the input
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        table = collections.defaultdict(list)
        for path in paths:
            data = path.split()
            root = data[0]
            for file in data[1:]:
                name, content = file.split('(')
                table[content[:-1]].append(root + '/' + name)
        
        return [x for x in table.values() if len(x) > 1]
