class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = 'qwertyuiopQWERTYUIOP'
        r2 = 'asdfghjklASDFGHJKL'
        r3 = 'zxcvbnmZXCVBNM'
        def isin(x):
            if x[0] in r1:
                row = r1
            elif x[0] in r2:
                row = r2
            else:
                row = r3
            return list(x) == list(filter(lambda ltr: ltr in row, x))
        return list(filter(lambda word: isin(word), words))