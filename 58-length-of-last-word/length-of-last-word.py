class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=[i for i in s.split(" ") if i!='']
        return len(s[-1])

        

