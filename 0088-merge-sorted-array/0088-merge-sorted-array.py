class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if n == 0:
            return

        i = n+m-1
        j = m-1
        k = n-1

        while i >= 0:
            if j < 0:
                nums1[i] = nums2[k]
                i -= 1
                k -= 1
                continue
            if k < 0:
                nums1[i] = nums1[j]
                i -= 1
                j -= 1
                continue
            if nums1[j] >= nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
                i -=1
                continue
            nums1[i] = nums2[k]
            k -= 1
            i -= 1
