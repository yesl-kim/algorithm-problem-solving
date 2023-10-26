class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ns = ''
        oc = 0
        cc = 0
        for x in s:
            if x.isalpha():
                ns += x
                continue
                
            if x == '(':
                ns += x
                oc += 1
            elif oc > cc:
                ns += x
                cc += 1
        
        if oc == cc:
            return ns
        
        s, ns = ns, ''
        oc = 0
        for x in s:
            if x != '(':
                ns += x
                continue
            if oc < cc:
                ns += x
                oc += 1
        return ns
                