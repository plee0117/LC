class Solution:
    def longestWord(self, words: List[str]) -> str:
        length = {}
        for word in words:
            if len(word) in length:
                length[len(word)].append(word)
            else:
                length[len(word)] = [word]
        l = 1
        shorter = ['']
        while l in length:
            longer = []
            for word in length[l]:
                if any(map(lambda x: x in word, shorter)):
                    longer.append(word)
            if not longer:
                break
            else:
                shorter = longer.copy()
                l += 1
        if shorter:
            shorter.sort()
            return shorter[0]
        else:
            return []