class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        res=[]
        start = 0
        for i in range(len(nums1)):
            for j in range(start, len(nums2)):
                if nums1[i]==nums2[j]:
                    start=j+1
                    res.append(nums1[i])
                    break
        return res