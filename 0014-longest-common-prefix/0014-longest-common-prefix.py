class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        res=strs[0]
        for s in strs:
            temp=''
            for i in range(len(res)):
                if res[i]!=s[i]: break
                temp+=res[i]
            res=temp
        return res