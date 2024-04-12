class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        substring = strs[0]
        for i in range(1, len(strs)):
            j=0
            while(j< len(substring) and j<len(strs[i]) and strs[i][j] == substring[j]):
                j+=1
            substring = substring[:j]
            if len(substring) ==0:
                return ""
        return substring
        