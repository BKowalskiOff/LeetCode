class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations  = []

        def _combine(k: int, nums: List[int], comb: List[int] = []) -> None:
            nonlocal combinations
            if k == 1:
                for num in nums:
                    combinations.append(comb + [num])
                return

            for i in range(len(nums)):
                _combine(k-1, nums[i+1:], comb + [nums[i]])

        _combine(k, [i for i in range(1,n+1)])
        return combinations
                