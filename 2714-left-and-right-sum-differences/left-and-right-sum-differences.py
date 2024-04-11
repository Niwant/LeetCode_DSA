class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[0] * len(nums)
        sumup = 0
        for i in range(len(nums)):
            res[i]=sumup
            sumup+=nums[i]
        sump=0
        for i in range(len(nums)-1,-1,-1):
            res[i] = abs(res[i]-sump)
            sump +=nums[i]

        return res 