class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        idx = 0
        jdx = len(letters)
        while jdx > idx:
            mid = (idx + jdx) // 2
            if target >= letters[mid]:
                idx = mid + 1
            else:
                jdx = mid
        return letters[jdx]