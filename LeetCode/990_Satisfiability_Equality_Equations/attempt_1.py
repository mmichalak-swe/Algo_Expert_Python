# O(n) time | O(1) space
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # populate table initially
        table = {char: char for char in 'abcdefghijklmnopqrstuvwxyz'}
        
        # create find function for easy lookup of groups
        # stop when char = table[char], return that char
        def find(char):
            if char != table[char]:
                table[char] = find(table[char])
            return table[char]

        # modify values of table to establish '==' relationships
        for a, e, _, b in equations:
            if e == '=':
                table[find(a)] = find(b)
        
        # if any values in find are equal, but equation wants a not equal relationship,
        # return False
        for a, e, _, b in equations:
            if e == '!' and find(a) == find(b):
                return False
        
        # if entire check is completed, all relationships are valid, return True
        return True
