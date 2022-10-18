# O(n*log(n) + n*w + m*3) time | O(n) space (for output)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        left = 0
        right = len(products) - 1
        output = []
        
        for i in range(len(searchWord)):
            searchChar = searchWord[i]
            
            while left <= right and (len(products[left]) <= i or products[left][i] != searchChar):
                left += 1
            
            while left <= right and (len(products[right]) <= i or products[right][i] != searchChar):
                right -= 1
            
            output.append([])
            for j in range(min(3, right - left + 1)):
                output[-1].append(products[left + j])
            
        return output
