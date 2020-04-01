class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        a = list(map(lambda x: str(x), range(1, n + 1)))
        a.sort()
        return a