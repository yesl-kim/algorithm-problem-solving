# mine
def threeSum(nums):
         nums.sort()
         n,hash,res=len(nums),{},[]

         for i in range(n-1):
             if nums[i]==nums[i+1]: continue

             for j in range(i+1,n):
                 x=nums[j]
                 c=hash.get(x)

                 if c:
                     res.append(c+[x])
                     del hash[x]
                 elif nums[j+1]==x:
                     continue
                 else:
                     hash[-(nums[i]+nums[j])]=[nums[i],nums[j]]

             hash.clear()
         return res