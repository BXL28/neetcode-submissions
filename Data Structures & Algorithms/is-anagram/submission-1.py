class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        news={}
        newt={}
        for i,dup in enumerate(s):
            if dup in news:
                news[dup]+=1
            else:
                news[dup]=1

        for i,dup in enumerate(t):
            if dup in newt:
                newt[dup]+=1
            else:
                newt[dup]=1

        return news==newt


            
