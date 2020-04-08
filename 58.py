class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(' ')
        if sum(list(map(lambda x: len(x), l))) == 0:
            return 0
        else:
            for w in l[::-1]:
                if len(w) > 0:
                    return len(w)