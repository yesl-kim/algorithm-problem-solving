class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        i=n-1
        while i<n:
            if i<0:
                digits.insert(0,1)
                break
            if digits[i]==9:
                digits[i]=0
                i-=1
            else:
                digits[i]+=1
                break
        return digits