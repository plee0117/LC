class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        pd = dict()
        wd = dict()

        for idx, ltr in enumerate(pattern):
            if ltr in pd and words[idx] in wd:
                if pd[ltr] == wd[words[idx]]:
                    continue
                else:
                    return False
            elif ltr not in pd and words[idx] not in wd:
                pd[ltr] = idx
                wd[words[idx]] = idx
            else:
                return False
        return True