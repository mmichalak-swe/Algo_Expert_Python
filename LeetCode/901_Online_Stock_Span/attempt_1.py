# O(n^2) time | O(n) space
# Will get TLE on LC
class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        
        span = 1
        for i in range(len(self.prices) - 2, -1, -1):
            if self.prices[i] <= price:
                span += 1
            else:
                break
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)