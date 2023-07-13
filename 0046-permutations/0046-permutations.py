class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def _permute(nums: List[int], permutation: List[int] = []) -> None:
            nonlocal permutations
            if len(nums) == 1:
                permutations.append(permutation + [nums[0]])
                return
            
            for i in range(len(nums)):
                _permute(nums[:i] + nums[i+1:], permutation + [nums[i]])

        _permute(nums)

        return permutations