class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_val = 0
        for acc in accounts:
            val = 0
            for j in acc: 
                val+=j
            max_val = max(max_val,val)
        return max_val
