class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m-1, n-1
        i = m + n - 1
        
        while 0 <= p1 and 0 <= p2:
            if nums1[p1] < nums2[p2]:
                nums1[i] = nums2[p2]
                p2-=1
            else:
                nums1[i] = nums1[p1]
                p1-=1
            i-=1
        
        if 0 <= p2:
            for i in range(p2+1):
                nums1[i] = nums2[i]
                