class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(lt,rt):
            while lt<rt:
                nums[lt], nums[rt] = nums[rt], nums[lt]
                lt += 1
                rt -= 1
        n=len(nums)
        k%=n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
       
