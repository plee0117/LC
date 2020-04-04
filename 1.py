class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        numsort = nums.copy()
        numsort.sort()
        print(numsort)
        i = 0
        while i < len(nums)-1:
            j = i + 1
            while j <len(nums):
                if numsort[i]+numsort[j] == target:
                    pos1 = nums.index(numsort[i])
                    pos2 = nums.index(numsort[j])
                    print(pos1,pos2)
                    if pos1 == pos2:
                        pos2 = nums[pos1 + 1:].index(numsort[j]) + pos1 + 1
                    return [pos1,pos2]
                elif numsort[i]+numsort[j] > target:
                    break
                j += 1
            i += 1