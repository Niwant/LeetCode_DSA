class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        para_list = []
        for i in range(0, len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                para_list.append(s[i])
            elif not len(para_list):
                return False
            elif ( s[i] == ")" and para_list.pop() != "(") or (s[i] =="]" and para_list.pop() != "[") or (s[i]=="}" and para_list.pop()!="{"):
                return False

        if len(para_list):
            return False
        return True
