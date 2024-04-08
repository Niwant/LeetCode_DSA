class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_dict = collections.defaultdict(int)
        j = 0
        for i in range(len(nums)):
            x = num_dict.get(nums[i], 0)
            if x < 2:
                nums[j]=nums[i]
                num_dict[nums[i]] = x+1
                j+=1
        return j     