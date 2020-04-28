class Solution:
    def countSegments(self, s: str) -> int:
        return len(list(filter(lambda x: x != '',s.split(' '))))