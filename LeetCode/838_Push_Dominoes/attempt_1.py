# O(n) time | O(n) space
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        res = []
        i = 0

        for j in range(1, len(dominoes)):
            if dominoes[j] == '.':
                continue
            middle = j - i - 1
            if i:
                res.append(dominoes[i])
            if dominoes[i] == dominoes[j]:
                res.append(dominoes[i] * middle)
            elif dominoes[i] == 'L' and dominoes[j] == 'R':
                res.append('.' * middle)
            else:
                res.append('R' * (middle // 2))
                res.append('.' * (middle % 2))
                res.append('L' * (middle // 2))

            i = j

        return ''.join(res)
