class Solution:
    def compress(self, chars: List[str]) -> int:
        l = len(chars)
        if l <= 1:
            pass
        else:
            ct = 0
            ltr = None
            for idx in range(l - 1, 0, -1):
                if ct == 0:
                    ltr = chars.pop(idx)
                    ct = 1
                elif chars[idx] == ltr:
                    chars.pop(idx)
                    ct += 1
                else:
                    if ct > 1:
                        for n in str(ct)[::-1]:
                            chars.insert(idx + 1, n)
                        chars.insert(idx + 1, ltr)
                    ltr = chars.pop(idx)
                    ct = 1
            if chars[0] == ltr:
                for n in str(ct + 1)[::-1]:
                    chars.insert(1, n)
            else:
                if ct > 1:
                    for n in str(ct)[::-1]:
                        chars.insert(1, n)
                chars.insert(1, ltr)
        return len(chars)