class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}
        for i, num in enumerate(nums):
            compl = target - num
            if compl in positions:
                return [positions[compl], i]
            positions[num] = i

