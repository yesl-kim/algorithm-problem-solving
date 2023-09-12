class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def dfs(s, sentence = ''):
            if not s:
                res.append(sentence.strip())
                return
            
            for w in wordDict:
                if s.startswith(w):
                    dfs(s[len(w):], sentence + ' ' + w)
            
        dfs(s)
        return res
            