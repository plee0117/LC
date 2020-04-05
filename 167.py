class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = i + 1
        length = len(numbers)
        while numbers[j] + numbers[i] < target and j < length - 1:
            j += 1
        if numbers[j] + numbers[i] == target:
            return [i + 1, j + 1]
        else:
            m = j
        i = 1
        while numbers[i] <= target:
            m = j
            while numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            else:
                i += 1