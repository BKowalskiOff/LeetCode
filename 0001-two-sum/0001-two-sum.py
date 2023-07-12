class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_map = {}
        for i, num in enumerate(nums):
            if  num in nums_map.keys():
                return [nums_map[num], i]
            else:
                nums_map[target - num] = i