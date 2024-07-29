class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a=list("qwertyuiop")
        b=list("asdfghjkl")
        c=list("zxcvbnm")
        k=[]
        def chk(s,l):
            return all(k in l for k in s.lower())
        for i in words:
            if chk(i,a) or chk(i,b) or chk(i,c)==True:
                k.append(i)
        return k

        
