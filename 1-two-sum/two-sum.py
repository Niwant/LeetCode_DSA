class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(0, len(nums)):
            if nums[i] in num_dict: 
                num_dict[nums[i]].append(i)
            else:
                num_dict[nums[i]] = [i]
        
        for i in range(0,len(nums)):
            if target-nums[i] in num_dict:
                if num_dict[target-nums[i]][0] == i: 
                    if len(num_dict[target-nums[i]])> 1 :
                        return [i,num_dict[target-nums[i]][1]]
                else:
                    return [i,num_dict[target-nums[i]][0]]