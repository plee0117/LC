class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        def compare(maxes,num):
            i = 0
            if num in maxes:
                return maxes
            
            while i < len(maxes):
                if num > maxes[i]:
                    maxes.insert(i, num)
                    return maxes[:3]
                else:
                    i += 1
            if len(maxes) < 3:
                maxes += [num]
            return maxes[:3]
        maxes = []
        for num in nums:
            maxes = compare(maxes, num)
            print(maxes)
        if len(maxes) == 3:
            return maxes[-1]
        else:
            return maxes[0]