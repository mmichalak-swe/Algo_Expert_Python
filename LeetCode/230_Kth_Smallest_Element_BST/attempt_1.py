# O(h + k) time | O(h) space, must go all the way down before visiting, so h time and space
class Solution:
    numVisited = 0
    lastValue = None

    def kthSmallest(self, root, k):
        
        def recursiveHelper(root, k):
            if root is None or self.numVisited >= k:
                return

            recursiveHelper(root.left, k)

            if self.numVisited == k:
                return

            self.numVisited += 1
            self.lastValue = root.val

            recursiveHelper(root.right, k)

        recursiveHelper(root, k)
        
        return self.lastValue
