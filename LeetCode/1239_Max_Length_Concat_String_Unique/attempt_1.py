# O(2^n) time | O(2^n) space
class Solution:
    def maxLength(self, arr: List[str]) -> int:

        # filter out all strings with duplicate characters
        unique = []
        for item in arr:
            itemSet = set(item)
            if len(itemSet) == len(item):
                unique.append(itemSet)

        concat = [set()]

        for u in unique:
            for c in concat:
                if not c & u:
                    concat.append(c | u)

        return max(len(cc) for cc in concat)
