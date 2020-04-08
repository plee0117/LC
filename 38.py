class Solution:
    def countAndSay(self, n: int) -> str:
        def change(nums):
            i = 0
            s = 0
            temp = ''
            while i < len(nums):
                c = 1
                while i + 1 < len(nums) and nums[s] == nums[i + 1]:
                    c += 1
                    i += 1
                temp = temp + str(c) +str(nums[s])
                s = i + 1
                i = s
            return temp
        
        nums = '1'
        for i in range(1,n):
            nums = change(nums)
            print(nums)
        return nums