import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_negative = [-x for x in nums]
        heapq.heapify(nums_negative)
        for i in range(k-1):
            heapq.heappop(nums_negative)
        return -heapq.heappop(nums_negative)