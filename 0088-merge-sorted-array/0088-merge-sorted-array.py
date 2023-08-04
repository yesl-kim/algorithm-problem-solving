class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 공간 재배치
        for i in range(m-1,-1,-1):
            nums1[n+i] = nums1[i]
        
        i = 0
        p1, p2 = n, 0
        while p1 < m + n and p2 < n:
            if nums1[p1] < nums2[p2]:
                nums1[i] = nums1[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1
            i += 1
        
        if p2 < n:
            for j in range(p2, n):
                nums1[i] = nums2[j]
                i += 1