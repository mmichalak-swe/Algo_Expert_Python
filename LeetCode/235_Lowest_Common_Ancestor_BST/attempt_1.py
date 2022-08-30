# O(log(n)) time | O(1) space
def lowestCommonAncestor(p, q):
    smaller = p.val if p.val < q.val else q.val
    larger = q.val if q.val > p.val else p.val

    while not (smaller <= root.val <= larger):
        if root.val > larger:
            root = root.left
        elif root.val < smaller:
            root = root.right
            
    return root
