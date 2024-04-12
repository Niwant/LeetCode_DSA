class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split(" ")
        if len(s)==1:
            return 1
        for i in range(len(res)-1 , -1 ,-1):
            if len(res[i]) >= 1:
                return len(res[i])

        

