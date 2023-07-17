class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash={}
        for n in nums:
            if n in hash:
                return True
            hash[n]=1
        return False
        