class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def notOrder(ldx, udx):
            if ldx > udx:
                return -1
            mid = (ldx + udx) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid] and target >= nums[ldx]:
                return inOrder(ldx, mid - 1)
            elif target > nums[mid] and target <= nums[udx]:
                return inOrder(mid + 1, udx)
            elif target < nums[mid]:
                if nums[mid] < nums[udx]:
                    return notOrder(ldx, mid - 1)
                else:
                    return notOrder(mid + 1, udx)
            elif target > nums[mid]:
                if nums[mid] > nums[udx]:
                    return notOrder(mid + 1, udx)
                else:
                    return notOrder(ldx, mid - 1)
        def inOrder(ldx, udx):
            while ldx <= udx:
                mid = (ldx + udx) // 2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    udx = mid - 1
                else:
                    ldx = mid + 1
            return -1
        if nums:
            return notOrder(0, len(nums) - 1)
        else:
            return -1