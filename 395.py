class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        dic = makedic(s)
        lis = [s]
        cont = 1
        while cont > 0:
            cont = 0
            for idx in range(len(lis)):
                tem, contem = check(lis[idx], k)
                lis += list(filter(lambda x: x != '', tem))
                cont += contem
                lis[idx] = ''
            lis = list(filter(lambda x: x != '', lis))
        if lis == []:
            return 0
        else:
            return max(len(c) for c in lis)

def makedic(s):
    dic = dict()
    for i in s:
        if i in dic:
            dic[i] += 1 
        else:
            dic[i] = 1
    return dic

def check(s, k):
    dic = makedic(s)
    if len(dic) == 0:
        return [s], False
    elif min(dic.values()) >= k:
        return [s], False
    else:
        lis = [s]
        for d in dic:
            if dic[d] < k:
                lis = splitem(lis, d)
        return lis, True

def splitem(lis, d):
    templis = list()
    for l in lis:
        templis += list(filter(lambda x: x != '', l.split(d)))
    return templis
