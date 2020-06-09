class Solution:

    def __init__(self, w: List[int]):
        self.pop = range(len(w))
        self.ws = w
        

    def pickIndex(self) -> int:
        return random.choices(self.pop, weights = self.ws)[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()