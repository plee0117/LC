class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words.sort(key = (lambda x: len(x)))
        ltrs = {}
        for i in licensePlate:
            if i.islower():
                if i in ltrs:
                    ltrs[i] += 1
                else:
                    ltrs[i] = 1
            elif i.isupper():
                if i.lower() in ltrs:
                    ltrs[i.lower()] += 1
                else:
                    ltrs[i.lower()] = 1
        for w in words:
            good = True
            for ltr, ct in ltrs.items():
                if w.count(ltr) < ct:
                    good = False
                    break
            if good:
                return w